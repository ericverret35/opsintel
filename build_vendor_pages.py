import os,re,yaml
from pathlib import Path
from datetime import datetime,timedelta,timezone,date

CVE_DIR=Path("cve"); VENDORS_DIR=Path("vendors"); BASE=os.getenv("SITE_BASE_URL","").rstrip("/")

def slugify(s,maxlen=80): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:maxlen]
def read_fm(path):
    with open(path,"r",encoding="utf-8") as f:
        lines=f.read().splitlines()
    if not lines or lines[0].strip()!="---": return {}
    fm=[]
    for ln in lines[1:]:
        if ln.strip()=="---": break
        fm.append(ln)
    return yaml.safe_load("\n".join(fm)) or {}

def week_start(d): return d-timedelta(days=d.weekday())

def svg_bars(weekly_counts):
    counts=[c for _,c in weekly_counts]; maxc=max(counts) if counts else 1
    W,H,PAD,GAP,BAR=12*20+20,80,10,6,12; scale=(H-2*PAD)/(maxc or 1); x=PAD; rects=[]
    for i,c in enumerate(counts):
        bh=max(2,int(c*scale)); y=H-PAD-bh
        rects.append(f'<rect x="{x}" y="{y}" width="{BAR}" height="{bh}" rx="2" fill="#2a7ae2"><title>W{i+1}: {c}</title></rect>')
        x+=BAR+GAP
    labels="".join([f'<text x="{PAD+i*(BAR+GAP)+BAR/2}" y="{H-2}" font-size="8" text-anchor="middle" fill="#666">{c}</text>' for i,c in enumerate(counts)])
    return f'<svg role="img" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">{"".join(rects)}{labels}</svg>'

def build():
    VENDORS_DIR.mkdir(parents=True,exist_ok=True)
    today=datetime.now(timezone.utc).date(); day30=today-timedelta(days=30); day90=today-timedelta(days=90)
    vendors={}
    for md in CVE_DIR.glob("*.md"):
        fm=read_fm(md)
        if not fm: continue
        dstr=str(fm.get("date","")[:10])
        try: d=datetime.fromisoformat(dstr).date()
        except: continue
        for v in (fm.get("vendors") or [])[:3]:
            vs=vendors.setdefault(v,{"items":[]})
            url=f"{BASE}/cve/{md.stem}/" if BASE else f"/cve/{md.stem}/"
            vs["items"].append({"date":d,"sev":(fm.get("severity") or"").upper(),"cvss":fm.get("cvss"),"title":fm.get("title") or md.stem,"url":url})

    def write_vendor_page(name,data):
        items=sorted(data["items"],key=lambda x:(x["date"],x.get("cvss") or 0),reverse=True)
        c30=sum(1 for x in items if x["date"]>=day30); c90=sum(1 for x in items if x["date"]>=day90)
        crit=sum(1 for x in items if x["sev"] in("CRITICAL","HIGH"))
        ws0=week_start(today); weeks=[ws0-timedelta(weeks=i) for i in range(11,-1,-1)]
        wmap={w:0 for w in weeks}
        for it in items:
            w=week_start(it["date"])
            if w in wmap: wmap[w]+=1
        weekly_counts=[(w,wmap[w]) for w in weeks]
        body=["---",f'title: "{name} vulnerabilities"','layout: default',"---\n",f"# {name} — {len(items)} CVEs","- 30j: {c30} | 90j: {c90} | Critical/High: {crit}\n",svg_bars(weekly_counts),"\n## Vulnérabilités récentes"]
        for it in items[:25]:
            tag=f"[{it['sev']}{' '+str(it['cvss']) if it.get('cvss') else ''}]".strip()
            body.append(f"- {tag} [{it['title']}]({it['url']}) — {it['date']}")
        VENDORS_DIR.joinpath(f"{slugify(name)}.md").write_text("\n".join(body),encoding="utf-8")

    for v,data in vendors.items(): write_vendor_page(v,data)
    ranking=[(sum(1 for x in data["items"] if x["date"]>=day90),v) for v,data in vendors.items()]
    ranking.sort(reverse=True)
    idx=["---",'title: "Vendors index"','layout: default',"---\n","# Vendors\n"]
    for c,v in ranking:
        link=f"{BASE}/vendors/{slugify(v)}/" if BASE else f"/vendors/{slugify(v)}/"
        idx.append(f"- [{v}]({link}) ({c})")
    (VENDORS_DIR/"index.md").write_text("\n".join(idx),encoding="utf-8")

if __name__=="__main__": build()
