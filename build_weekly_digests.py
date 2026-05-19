import os,yaml
from pathlib import Path
from datetime import datetime,timedelta,timezone,date

DIRS={"cve":"cve","outages":"outages","papers":"papers","advisories":"advisories","jobs":"jobs","pricing":"pricing","conferences":"conferences"}
OUT_DIR=Path("weekly"); BASE=os.getenv("SITE_BASE_URL","").rstrip("/")

def read_fm(path):
    t=path.read_text(encoding="utf-8").splitlines()
    if not t or t[0].strip()!="---": return {}
    fm=[]
    for ln in t[1:]:
        if ln.strip()=="---": break
        fm.append(ln)
    return yaml.safe_load("\n".join(fm)) or {}

def last_completed_week():
    today=datetime.now(timezone.utc).date()
    start=today-timedelta(days=today.weekday()+7); end=start+timedelta(days=6)
    iso_year,iso_week,_=start.isocalendar()
    return start,end,iso_year,iso_week

def main():
    start,end,y,w=last_completed_week(); OUT_DIR.mkdir(exist_ok=True)
    items_cve,items_out,items_pp,items_adv,items_jobs,items_conf=[],[],[],[],[],[]
    def add_items(coll,dir_key,items_list,fields,url_prefix):
        for p in Path(DIRS[dir_key]).glob("*.md"):
            fm=read_fm(p); d=str(fm.get("date","")[:10])
            if not d: continue
            try: dd=datetime.fromisoformat(d).date()
            except: continue
            if start<=dd<=end:
                vals=[fm.get(f) for f in fields]
                url=f"{BASE}/{url_prefix}/{p.stem}/" if BASE else f"/{url_prefix}/{p.stem}/"
                items_list.append(tuple(vals)+((fm.get("kev",False) if "kev" in fields else False),url))

    add_items("cve","cve",items_cve,["severity","cvss","title"],  "cve")
    add_items("outages","outages",items_out,["severity","vendor","title"], "outages")
    add_items("papers","papers",items_pp,["title"], "ai")
    add_items("advisories","advisories",items_adv,["severity","cvss","ecosystem","osv_id","title"], "advisories")
    add_items("jobs","jobs",items_jobs,["title","company","remote"], "jobs")
    add_items("conferences","conferences",items_conf,["conference","location","cfp_deadline","url"], "conf")

    sev_rank={"CRITICAL":2,"HIGH":1}; items_cve.sort(key=lambda x:(sev_rank.get(x[0],0),x[1],x[-1]),reverse=True)
    items_out.sort(key=lambda x:(1 if x[0]=="major" else 0,len(items_out)-items_out.index(x)),reverse=True)
    sev_rank_adv={"CRITICAL":3,"HIGH":2,"MEDIUM":1}; items_adv.sort(key=lambda x:(sev_rank_adv.get(x[0],0),x[1]),reverse=True)

    body=["---",f'title: "OpsIntel Weekly {y}-W{w:02d}"',f'date: "{end.isoformat()}"','layout: default',"---\n",f"# OpsIntel Weekly — {y}-W{w:02d}\n","## 🔐 CVE Top"]
    for sev,cvss,title,kev,url in items_cve[:15]: body.append(f"- [{sev} {cvss:g}]{' (KEV)' if kev else ''} {title} → {url}")
    body.append("\n## 🚨 Incidents Major")
    for sev,vendor,title,_,url in items_out[:10]:
        if sev=="major": body.append(f"- {vendor}: {title} → {url}")
    body.append("\n## 🤖 AI Papers")
    for title,url in items_pp[:10]: body.append(f"- {title} → {url}")
    body.append("\n## 🛡️ Advisories")
    for sev,cvss,eco,osv_id,_,url in items_adv[:15]: body.append(f"- [{eco}] {sev} {cvss:g} {osv_id} → {url}")
    body.append("\n## 💼 Jobs Remote")
    for title,company,remote,url in items_jobs[:10]:
        if remote: body.append(f"- {title} @ {company} → {url}")
    body.append("\n## 📅 Conferences")
    for name,location,cfp,url in items_conf[:10]: body.append(f"- {name} ({location}) CFP: {cfp or 'N/A'} → {url}")
    OUT_DIR.joinpath(f"{y}-W{w:02d}.md").write_text("\n".join(body),encoding="utf-8")
    print("Weekly page generated:",f"{y}-W{w:02d}.md")

if __name__=="__main__": main()
