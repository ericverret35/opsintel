import io,json,zipfile,requests,re
from pathlib import Path
from datetime import datetime,timedelta,timezone

OUT_DIR=Path("advisories"); STATE=Path("data/osv_seen.json"); STATE.parent.mkdir(parents=True,exist_ok=True)
BASE="https://osv-vulnerabilities.storage.googleapis.com"
ECOS=["PyPI","npm","Go","Maven","crates.io","RubyGems"]; LOOKBACK_DAYS=2; MAX_PER_RUN=120

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:80]
def is_recent(v):
    dt_str=v.get("modified") or v.get("published")
    if not dt_str: return False
    try: d=datetime.fromisoformat(dt_str.replace("Z","+00:00"))
    except: return False
    return d>=datetime.now(timezone.utc)-timedelta(days=LOOKBACK_DAYS)
def highest_severity(v):
    sev=v.get("severity") or []; best=None; best_score=-1
    for s in sev:
        try: score=float(s.get("score") or 0)
        except: score=0
        label="CRITICAL" if score>=9 else "HIGH" if score>=7 else "MEDIUM" if score>=4 else "LOW" if score>0 else ""
        if score>best_score: best_score=score; best=(label,score)
    return best or ("",None)

def read_state():
    if STATE.exists():
        try: return set(json.loads(STATE.read_text(encoding="utf-8")))
        except: return set()
    return set()
def write_state(ids): STATE.write_text(json.dumps(sorted(list(ids))),encoding="utf-8")

def write_post(v,eco):
    import yaml
    vid=v.get("id"); published=(v.get("published") or v.get("modified") or datetime.utcnow().date().isoformat())[:10]
    pkgs=[a.get("package",{}).get("name","") for a in v.get("affected",[]) if a.get("package",{}).get("name")]
    pkg=pkgs[0] if pkgs else "multiple"; sev_label,sev_score=highest_severity(v)
    title=f"{vid} — {eco} {pkg}"; tags=[eco.lower()]+([sev_label.lower()] if sev_label else [])
    links=[r["url"] for r in v.get("references",[]) if r.get("url")]; desc=(v.get("summary") or v.get("details") or"").strip()
    body=["---",f'title: "{title}"',f'date: "{published}"',"layout: post",'category: "advisory"',f'osv_id: "{vid}"',f'ecosystem: "{eco}"',f'packages: {json.dumps(pkgs,ensure_ascii=False)}']
    if sev_label: body.append(f'severity: "{sev_label}"')
    if sev_score is not None: body.append(f'cvss: {sev_score}')
    if links: body.append("links: "+json.dumps(links))
    body.append(f"tags: {json.dumps(tags)}"); body.append("---\n")
    if desc: body.append(desc+"\n")
    if links: body.append("## References\n"+"".join(f"- {u}\n" for u in links[:10])+"\n")
    OUT_DIR.mkdir(parents=True,exist_ok=True)
    Path(OUT_DIR/f"{published}-{slugify(vid)}.md").write_text("\n".join(body),encoding="utf-8")

def main():
    seen=read_state(); created=0
    for eco in ECOS:
        url=f"{BASE}/{eco}/all.zip"
        try:
            r=requests.get(url,timeout=120)
            if r.status_code!=200: print("Skip",eco,r.status_code); continue
            z=zipfile.ZipFile(io.BytesIO(r.content))
        except Exception as e: print("Zip error",eco,e); continue
        for name in z.namelist():
            if not name.endswith(".json"): continue
            try: v=json.loads(z.read(name))
            except: continue
            vid=v.get("id")
            if not vid or vid in seen: continue
            if not is_recent(v): continue
            write_post(v,eco); seen.add(vid); created+=1
            if created>=MAX_PER_RUN: break
        if created>=MAX_PER_RUN: break
    write_state(seen); print(f"OSV advisories created: {created}")

if __name__=="__main__": main()
