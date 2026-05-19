import os,requests,argparse
from pathlib import Path
from datetime import datetime,timedelta,timezone
import yaml

def read_fm(path):
    t=path.read_text(encoding="utf-8").splitlines()
    if not t or t[0].strip()!="---": return {}
    fm=[]
    for ln in t[1:]:
        if ln.strip()=="---": break
        fm.append(ln)
    return yaml.safe_load("\n".join(fm)) or {}

def pick_highlights(site,look_cve_h=26,look_out_m=120):
    now=datetime.now(timezone.utc); out=[]
    cves=[]
    for p in Path("cve").glob("*.md"):
        fm=read_fm(p); sev=(fm.get("severity") or"").upper(); cvss=float(fm.get("cvss") or 0)
        if sev not in("CRITICAL","HIGH"): continue
        if sev=="HIGH" and cvss<8.0: continue
        mtime=datetime.fromtimestamp(p.stat().st_mtime,tz=timezone.utc)
        if mtime<now-timedelta(hours=look_cve_h): continue
        cves.append((sev,cvss,fm.get("title",""),f"{site}/cve/{p.stem}/" if site else f"/cve/{p.stem}/",bool(fm.get("kev",False))))
    cves.sort(key=lambda x:(x[0]=="CRITICAL",x[1],x[4]),reverse=True)
    for sev,cvss,title,url,kev in cves[:2]:
        tag=f"{sev} {cvss:g}"; k=" • KEV" if kev else ""; out.append(f"CVE {tag}{k}: {title} → {url}")
    majors=[]
    for p in Path("outages").glob("*.md"):
        fm=read_fm(p)
        if (fm.get("severity") or"").lower()!="major": continue
        mtime=datetime.fromtimestamp(p.stat().st_mtime,tz=timezone.utc)
        if mtime<now-timedelta(minutes=look_out_m): continue
        majors.append((fm.get("vendor","Service"),fm.get("title","incident"),fm.get("link") or(f"{site}/outages/{p.stem}/" if site else f"/outages/{p.stem}/")))
    majors=majors[:1]
    for vendor,title,link in majors: out.append(f"Incident major — {vendor}: {title} → {link}")
    papers=[]
    for p in Path("papers").glob("*.md"):
        fm=read_fm(p); d=fm.get("date")
        if not d: continue
        try: dd=datetime.fromisoformat(str(d)[:10]).date()
        except: continue
        if dd>=(now.date()-timedelta(days=1)): papers.append((fm.get("title",""),fm.get("link") or(f"{site}/ai/{p.stem}/" if site else f"/ai/{p.stem}/")))
    if papers:
        t,l=papers[0]; out.append(f"AI paper: {t} → {l}")
    jobs=[]
    for p in Path("jobs").glob("*.md"):
        fm=read_fm(p); d=fm.get("date")
        if not d or not fm.get("remote",False): continue
        try: dd=datetime.fromisoformat(str(d)[:10]).date()
        except: continue
        if dd>=(now.date()-timedelta(days=1)): jobs.append((fm.get("title",""),fm.get("company",""),f"{site}/jobs/{p.stem}/" if site else f"/jobs/{p.stem}/"))
    if jobs:
        t,c,l=jobs[0]; out.append(f"💼 Job remote: {t} @ {c} → {l}")
    return out

def make_post_text(lines,site):
    head="Brief du jour 🔎"; more=f"Plus: {site}" if site else ""
    text=head+"\n"+"\n".join(f"• {ln}" for ln in lines)+("\n"+more if lines and more else "")
    if len(text)>300: text=text[:295].rsplit(" ",1)[0]+"…"
    return text

def post_masto(base,token,text):
    if not base or not token: return None
    url=base.rstrip("/")+"/api/v1/statuses"; r=requests.post(url,data={"status":text},headers={"Authorization":f"Bearer {token}"},timeout=30)
    print("Mastodon:",r.status_code); return r.ok

def post_bsky(handle,app_password,text):
    if not handle or not app_password: return None
    s=requests.Session()
    r=s.post("https://bsky.social/xrpc/com.atproto.server.createSession",json={"identifier":handle,"password":app_password},timeout=30)
    if r.status_code!=200: print("Bluesky failed:",r.status_code,r.text[:200]); return False
    data=r.json(); did=data["did"]; jwt=data["accessJwt"]
    record={"$type":"app.bsky.feed.post","text":text,"createdAt":datetime.utcnow().replace(tzinfo=timezone.utc).isoformat().replace("+00:00","Z"),"langs":["fr"]}
    r2=s.post("https://bsky.social/xrpc/com.atproto.repo.createRecord",headers={"Authorization":f"Bearer {jwt}"},json={"repo":did,"collection":"app.bsky.feed.post","record":record},timeout=30)
    print("Bluesky:",r2.status_code); return r2.ok

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--preview",action="store_true"); args=parser.parse_args()
    site=os.getenv("SITE_BASE_URL","").rstrip("/")
    lines=pick_highlights(site)
    if not lines: print("No highlights."); return
    text=make_post_text(lines,site); print("Post preview:\n",text)
    if args.preview: return
    post_masto(os.getenv("MASTO_BASE"),os.getenv("MASTO_TOKEN"),text)
    post_bsky(os.getenv("BLUESKY_HANDLE"),os.getenv("BLUESKY_APP_PASSWORD"),text)

if __name__=="__main__": main()
