import os,yaml
from pathlib import Path
from datetime import datetime,timedelta,timezone,date

OUT_DIR=Path("advisories-weekly"); BASE=os.getenv("SITE_BASE_URL","").rstrip("/")

def read_fm(path):
    t=path.read_text(encoding="utf-8").splitlines()
    if not t or t[0].strip()!="---": return {}
    fm=[]
    for ln in t[1:]:
        if ln.strip()=="---": break
        fm.append(ln)
    return yaml.safe_load("\n".join(fm)) or {}

def last_completed_week():
    today=datetime.now(timezone.utc).date(); start=today-timedelta(days=today.weekday()+7); end=start+timedelta(days=6)
    iso_year,iso_week,_=start.isocalendar()
    return start,end,iso_year,iso_week

def main():
    start,end,y,w=last_completed_week(); OUT_DIR.mkdir(exist_ok=True); items=[]
    for p in Path("advisories").glob("*.md"):
        fm=read_fm(p); d=str(fm.get("date","")[:10])
        if not d: continue
        try: dd=datetime.fromisoformat(d).date()
        except: continue
        if start<=dd<=end:
            sev=(fm.get("severity") or"").upper(); cvss=float(fm.get("cvss") or 0)
            eco=fm.get("ecosystem",""); osv_id=fm.get("osv_id","")
            url=f"{BASE}/advisories/{p.stem}/" if BASE else f"/advisories/{p.stem}/"
            items.append((sev,cvss,eco,osv_id,fm.get("title",""),url))
    sev_rank={"CRITICAL":3,"HIGH":2,"MEDIUM":1}; items.sort(key=lambda x:(sev_rank.get(x[0],0),x[1]),reverse=True)
    eco_counts={}; [eco_counts.update({eco:eco_counts.get(eco,0)+1}) for _,_,eco,*_ in items]
    body=["---",f'title: "Advisories Weekly {y}-W{w:02d}"',f'date: "{end.isoformat()}"','layout: default',"---\n",f"# Security Advisories Weekly — {y}-W{w:02d}\n",f"Total: {len(items)}\n","## Par écosystème\n"]
    for eco,count in sorted(eco_counts.items(),key=lambda x:x[1],reverse=True): body.append(f"- {eco}: {count}")
    body.append("\n## Top advisories\n")
    if not items: body.append("Aucune cette semaine.")
    else:
        for sev,cvss,eco,osv_id,_,url in items[:50]:
            tag=f"[{eco}]" if eco else ""; score=f"{sev} {cvss:g}" if sev else ""
            body.append(f"- {tag} {score} {osv_id} → {url}")
    OUT_DIR.joinpath(f"{y}-W{w:02d}.md").write_text("\n".join(body),encoding="utf-8")
    print("Advisories weekly generated:",f"{y}-W{w:02d}.md")

if __name__=="__main__": main()
