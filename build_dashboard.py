import json,yaml
from pathlib import Path
from datetime import datetime,timedelta,timezone,date
from collections import Counter

def read_fm(path):
    t=path.read_text(encoding="utf-8").splitlines()
    if not t or t[0].strip()!="---": return {}
    fm=[]
    for ln in t[1:]:
        if ln.strip()=="---": break
        fm.append(ln)
    return yaml.safe_load("\n".join(fm)) or {}

def coll_stats(base_dir,date_field="date",sev_field="severity",extra_field=None):
    total=total_7d=total_30d=critical=high=kev=0; by_week=Counter(); extra_count=0
    for p in Path(base_dir).glob("*.md"):
        fm=read_fm(p); dstr=str(fm.get(date_field,"")[:10])
        if not dstr: continue
        try: d=datetime.fromisoformat(dstr).date()
        except: continue
        total+=1
        if d>=day7: total_7d+=1
        if d>=day30: total_30d+=1
        sev=(fm.get(sev_field,"") or"").upper()
        if sev=="CRITICAL": critical+=1
        elif sev=="HIGH": high+=1
        if fm.get("kev"): kev+=1
        y,w,_=d.isocalendar(); by_week[f"{y}-W{w:02d}"]+=1
        if extra_field:
            val=fm.get(extra_field,False)
            if val: extra_count+=1
    return {"total":total,"last_7d":total_7d,"last_30d":total_30d,"critical":critical,"high":high,"kev":kev,"weekly":{"labels":weeks_labels,"data":[by_week.get(k,0) for k in weeks_keys]},"extra":extra_count,"by_week":by_week}

def main():
    now_d=datetime.now(timezone.utc).date(); day7=now_d-timedelta(days=7); day30=now_d-timedelta(days=30)
    global weeks_keys,weeks_labels; weeks_keys=[]; weeks_labels=[]
    for i in range(11,-1,-1):
        d=now_d-timedelta(weeks=i); y,w,_=d.isocalendar(); weeks_keys.append(f"{y}-W{w:02d}"); weeks_labels.append(f"W{w:02d}")
    cve=coll_stats("cve","date","severity","kev")
    out=coll_stats("outages","date","severity")
    pap=coll_stats("papers","date","category")
    adv=coll_stats("advisories","date","severity")
    git=coll_stats("github_trending","date","language")
    news=coll_stats("tech_news","date","source")
    jobs=coll_stats("jobs","date","company","remote")
    k8s=coll_stats("k8s_releases","date","tool")
    pod=coll_stats("podcasts","date","source")
    pri=coll_stats("pricing","date","tool")
    ctf=coll_stats("ctf","date","source")
    conf=coll_stats("conferences","date","conference")
    vendor_counts=Counter()
    for p in Path("cve").glob("*.md"):
        fm=read_fm(p)
        for v in (fm.get("vendors") or [])[:3]: vendor_counts[v]+=1
    outages_by_vendor=Counter()
    for p in Path("outages").glob("*.md"):
        fm=read_fm(p); outages_by_vendor[fm.get("vendor","Unknown")]+=1
    stats={"cve":{"total":cve["total"],"last_7d":cve["last_7d"],"last_30d":cve["last_30d"],"critical":cve["critical"],"high":cve["high"],"kev":cve["kev"],"weekly":cve["weekly"],"top_vendors":[{"name":v,"count":c} for v,c in vendor_counts.most_common(10)]},"outages":{"total":out["total"],"last_7d":out["last_7d"],"major":out["extra"],"by_vendor":[{"name":v,"count":c} for v,c in outages_by_vendor.most_common(10)]},"papers":{"total":pap["total"],"last_7d":pap["last_7d"]},"advisories":{"total":adv["total"],"last_7d":adv["last_7d"],"critical":adv["critical"],"high":adv["high"],"by_ecosystem":[{"name":e,"count":c} for e,c in adv["by_week"].most_common(10)]},"github":{"total":git["total"],"last_7d":git["last_7d"]},"news":{"total":news["total"],"last_7d":news["last_7d"]},"jobs":{"total":jobs["total"],"last_7d":jobs["last_7d"],"remote":jobs["extra"]},"k8s":{"total":k8s["total"],"last_7d":k8s["last_7d"]},"podcasts":{"total":pod["total"],"last_7d":pod["last_7d"]},"pricing":{"total":pri["total"],"last_7d":pri["last_7d"]},"ctf":{"total":ctf["total"],"last_7d":ctf["last_7d"]},"conferences":{"total":conf["total"],"upcoming":conf["last_30d"]},"updated":datetime.now(timezone.utc).isoformat()}
    Path("assets").mkdir(exist_ok=True)
    Path("assets/dashboard.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding="utf-8")
    print("Dashboard data generated:",stats["updated"])

if __name__=="__main__": main()
