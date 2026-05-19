import json, yaml
from pathlib import Path
from datetime import datetime, timedelta, timezone
from collections import Counter

def read_fm(path):
t = path.read_text(encoding="utf-8").splitlines()
if not t or t[0].strip()!="---"):
return {}
fm=[]
for ln in t[1:]:
if ln.strip()=="---"):
break
fm.append(ln)
return yaml.safe_load("\n".join(fm)) or {}

def make_weeks(today, n=12):
keys=[]; labels=[]
for i in range(n-1,-1,-1):
d=today - timedelta(weeks=i)
y,w,_=d.isocalendar()
keys.append(f"{y}-W{w:02d}")
labels.append(f"W{w:02d}")
return keys,labels

def coll_stats(base_dir, *, date_field="date", severity_field=None, count_field=None, extra_pred=None, weeks_keys=None, weeks_labels=None, today=None):
if today is None:
today = datetime.now(timezone.utc).date()
day7 = today - timedelta(days=7)
day30 = today - timedelta(days=30)

texte

total=total_7d=total_30d=critical=high=kev=0
by_week = Counter()
by_attr = Counter()
extra_count = 0

for p in Path(base_dir).glob("*.md"):
    fm = read_fm(p)
    dstr = str(fm.get(date_field,"")[:10])
    if not dstr: 
        continue
    try:
        d = datetime.fromisoformat(dstr).date()
    except:
        continue

    total += 1
    if d>=day7: total_7d += 1
    if d>=day30: total_30d += 1

    if severity_field:
        sev = str(fm.get(severity_field,"")).upper()
        if sev == "CRITICAL": critical += 1
        elif sev == "HIGH": high += 1

    if fm.get("kev"): 
        kev += 1

    y,w,_ = d.isocalendar()
    by_week[f"{y}-W{w:02d}"] += 1

    if count_field:
        val = fm.get(count_field)
        if isinstance(val, list):
            for v in val:
                if v: by_attr[str(v)] += 1
        elif val:
            by_attr[str(val)] += 1

    if extra_pred and extra_pred(fm):
        extra_count += 1

if weeks_keys is None or weeks_labels is None:
    weeks_keys, weeks_labels = make_weeks(today)

weekly = {"labels": weeks_labels, "data": [by_week.get(k,0) for k in weeks_keys]}

return {"total": total, "last_7d": total_7d, "last_30d": total_30d, "critical": critical, "high": high, "kev": kev, "weekly": weekly, "extra": extra_count, "by_attr": by_attr}
def main():
today = datetime.now(timezone.utc).date()
weeks_keys, weeks_labels = make_weeks(today)

texte

cve = coll_stats("cve", date_field="date", severity_field="severity", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
out = coll_stats("outages", date_field="date", severity_field="severity", extra_pred=lambda fm: str(fm.get("severity","")).lower()=="major", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
pap = coll_stats("papers", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
adv = coll_stats("advisories", date_field="date", severity_field="severity", count_field="ecosystem", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
git = coll_stats("github_trending", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
news = coll_stats("tech_news", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
jobs = coll_stats("jobs", date_field="date", extra_pred=lambda fm: bool(fm.get("remote")), weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
k8s = coll_stats("k8s_releases", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
pod = coll_stats("podcasts", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
pri = coll_stats("pricing", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
ctf = coll_stats("ctf", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)
conf = coll_stats("conferences", date_field="date", weeks_keys=weeks_keys, weeks_labels=weeks_labels, today=today)

vendor_counts = Counter()
for p in Path("cve").glob("*.md"):
    fm=read_fm(p)
    for v in (fm.get("vendors") or [])[:3]:
        vendor_counts[v]+=1

outages_by_vendor = Counter()
for p in Path("outages").glob("*.md"):
    fm=read_fm(p)
    outages_by_vendor[fm.get("vendor","Unknown")] += 1

upcoming = 0
for p in Path("conferences").glob("*.md"):
    fm = read_fm(p)
    dstr = str(fm.get("event_date") or fm.get("date") or "")[:10]
    try: d = datetime.fromisoformat(dstr).date()
    except: continue
    if d >= today:
        upcoming += 1

stats = {
    "cve": {"total": cve["total"], "last_7d": cve["last_7d"], "last_30d": cve["last_30d"], "critical": cve["critical"], "high": cve["high"], "kev": cve["kev"], "weekly": cve["weekly"], "top_vendors": [{"name": v, "count": c} for v,c in vendor_counts.most_common(10)]},
    "outages": {"total": out["total"], "last_7d": out["last_7d"], "major": out["extra"], "by_vendor": [{"name": v, "count": c} for v,c in outages_by_vendor.most_common(10)]},
    "papers": {"total": pap["total"], "last_7d": pap["last_7d"]},
    "advisories": {"total": adv["total"], "last_7d": adv["last_7d"], "critical": {"count": adv["critical"]}, "high": {"count": adv["high"]}, "by_ecosystem": [{"name": e, "count": c} for e,c in adv["by_attr"].most_common(10)]},
    "github": {"total": git["total"], "last_7d": git["last_7d"]},
    "news": {"total": news["total"], "last_7d": news["last_7d"]},
    "jobs": {"total": jobs["total"], "last_7d": jobs["last_7d"], "remote": jobs["extra"]},
    "k8s": {"total": k8s["total"], "last_7d": k8s["last_7d"]},
    "podcasts": {"total": pod["total"], "last_7d": pod["last_7d"]},
    "pricing": {"total": pri["total"], "last_7d": pri["last_7d"]},
    "ctf": {"total": ctf["total"], "last_7d": ctf["last_7d"]},
    "conferences": {"total": conf["total"], "upcoming": upcoming},
    "updated": datetime.now(timezone.utc).isoformat()
}

Path("assets").mkdir(exist_ok=True)
Path("assets/dashboard.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
print("Dashboard data generated:", stats["updated"])
si nom ==" main ":
main()
