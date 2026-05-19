import os,json,yaml
from pathlib import Path

BASE=os.getenv("SITE_BASE_URL","").rstrip("/")

def read_fm(p):
    t=p.read_text(encoding="utf-8").splitlines()
    if not t or t[0].strip()!="---": return {}
    fm=[]
    for ln in t[1:]:
        if ln.strip()=="---": break
        fm.append(ln)
    return yaml.safe_load("\n".join(fm)) or {}

def make_url(coll,stem): return f"{BASE}/{coll}/{stem}/" if BASE else f"/{coll}/{stem}/"

def top_cves(n=50):
    out=[]
    for p in Path("cve").glob("*.md"):
        fm=read_fm(p); out.append({"id":(fm.get("title","").split(" — ")or[""])[0],"title":fm.get("title"),"severity":fm.get("severity"),"cvss":fm.get("cvss"),"vendors":fm.get("vendors") or [],"url":make_url("cve",p.stem),"kev":bool(fm.get("kev",False)),"date":fm.get("date")})
    out.sort(key=lambda x:((x["severity"] in("CRITICAL","HIGH")),float(x["cvss"] or 0),x["date"]),reverse=True)
    return out[:n]

def major_outages(n=100):
    out=[]
    for p in Path("outages").glob("*.md"):
        fm=read_fm(p)
        if (fm.get("severity") or"").lower()!="major": continue
        out.append({"vendor":fm.get("vendor"),"title":fm.get("title"),"url":make_url("outages",p.stem),"ext":fm.get("link"),"date":fm.get("date")})
    out.sort(key=lambda x:x["date"] or"",reverse=True)
    return out[:n]

def latest_papers(n=50):
    out=[]
    for p in Path("papers").glob("*.md"):
        fm=read_fm(p); out.append({"title":fm.get("title"),"authors":fm.get("authors") or [],"url":make_url("ai",p.stem),"ext":fm.get("link"),"cat":fm.get("arxiv_category"),"date":fm.get("date")})
    out.sort(key=lambda x:x["date"] or"",reverse=True)
    return out[:n]

def top_advisories(n=100):
    out=[]
    for p in Path("advisories").glob("*.md"):
        fm=read_fm(p); out.append({"osv_id":fm.get("osv_id"),"title":fm.get("title"),"ecosystem":fm.get("ecosystem"),"severity":fm.get("severity"),"cvss":fm.get("cvss"),"packages":fm.get("packages") or [],"url":make_url("advisories",p.stem),"date":fm.get("date")})
    out.sort(key=lambda x:((x["severity"] in("CRITICAL","HIGH")),float(x["cvss"] or 0),x["date"]),reverse=True)
    return out[:n]

def vendor_stats():
    stats={}
    for p in Path("cve").glob("*.md"):
        fm=read_fm(p)
        for v in fm.get("vendors") or []:
            s=stats.setdefault(v,{"count":0,"latest":None}); s["count"]+=1; s["latest"]=max(s["latest"],fm.get("date")) if s["latest"] else fm.get("date")
    return stats

def latest_jobs(n=50):
    out=[]
    for p in Path("jobs").glob("*.md"):
        fm=read_fm(p); out.append({"title":fm.get("title"),"company":fm.get("company"),"url":make_url("jobs",p.stem),"remote":fm.get("remote",False),"date":fm.get("date")})
    out.sort(key=lambda x:x["date"] or"",reverse=True)
    return out[:n]

def latest_pricing(n=50):
    out=[]
    for p in Path("pricing").glob("*.md"):
        fm=read_fm(p); out.append({"tool":fm.get("tool"),"title":fm.get("title"),"url":make_url("pricing",p.stem),"date":fm.get("date")})
    out.sort(key=lambda x:x["date"] or"",reverse=True)
    return out[:n]

def main():
    api=Path("api"); api.mkdir(exist_ok=True)
    Path(api/"cve_latest.json").write_text(json.dumps(top_cves(),ensure_ascii=False),encoding="utf-8")
    Path(api/"outages_major.json").write_text(json.dumps(major_outages(),ensure_ascii=False),encoding="utf-8")
    Path(api/"papers_latest.json").write_text(json.dumps(latest_papers(),ensure_ascii=False),encoding="utf-8")
    Path(api/"advisories_latest.json").write_text(json.dumps(top_advisories(),ensure_ascii=False),encoding="utf-8")
    Path(api/"vendors.json").write_text(json.dumps(vendor_stats(),ensure_ascii=False),encoding="utf-8")
    Path(api/"jobs_latest.json").write_text(json.dumps(latest_jobs(),ensure_ascii=False),encoding="utf-8")
    Path(api/"pricing_latest.json").write_text(json.dumps(latest_pricing(),ensure_ascii=False),encoding="utf-8")
    print("API JSON built.")

if __name__=="__main__": main()
