import os,argparse,requests,yaml
from pathlib import Path
from datetime import datetime,timedelta,timezone

def read_fm(path):
    with open(path,"r",encoding="utf-8") as f:
        lines=f.read().splitlines()
    if not lines or lines[0].strip()!="---": return {}
    out=[]
    for ln in lines[1:]:
        if ln.strip()=="---": break
        out.append(ln)
    return yaml.safe_load("\n".join(out)) or {}

def link_to(base,coll,stem):
    base=(base or"").rstrip("/"); return f"{base}/{coll}/{stem}/" if base else f"/{coll}/{stem}/"

def post_slack(url,text): return requests.post(url,json={"text":text},timeout=20)
def post_discord(url,text): return requests.post(url,json={"content":text},timeout=20)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--cve",type=int,default=0); ap.add_argument("--outages",type=int,default=0); ap.add_argument("--jobs",type=int,default=0); args=ap.parse_args()
    SLACK=os.getenv("SLACK_WEBHOOK_URL"); DISCORD=os.getenv("DISCORD_WEBHOOK_URL"); SITE=os.getenv("SITE_BASE_URL","").strip()
    now=datetime.now(timezone.utc); lines=[]
    if args.cve>0:
        th=now-timedelta(hours=args.cve); cve_lines=[]
        for p in Path("cve").glob("*.md"):
            fm=read_fm(p); sev=(fm.get("severity") or"").upper(); cvss=fm.get("cvss") or 0
            if sev not in("CRITICAL","HIGH"): continue
            if sev=="HIGH" and float(cvss or 0)<8.0: continue
            mtime=datetime.fromtimestamp(p.stat().st_mtime,tz=timezone.utc)
            if mtime<th: continue
            url=link_to(SITE,"cve",p.stem); vendors=", ".join((fm.get("vendors") or[])[:3])
            cve_lines.append(f"• [{sev} {cvss}] {fm.get('title','')} — {vendors or'n/a'} → {url}")
        if cve_lines: lines.append("*Sécurité — CVE critiques/élevées*"); lines.extend(sorted(cve_lines)[:10])
    if args.outages>0:
        th=now-timedelta(minutes=args.outages); out_lines=[]
        for p in Path("outages").glob("*.md"):
            fm=read_fm(p); sev=(fm.get("severity") or"").lower()
            if sev!="major": continue
            mtime=datetime.fromtimestamp(p.stat().st_mtime,tz=timezone.utc)
            if mtime<th: continue
            url_local=link_to(SITE,"outages",p.stem); ext=fm.get("link")
            out_lines.append(f"• {fm.get('vendor','Service')}: {fm.get('title','incident')} → {ext or url_local}")
        if out_lines: lines.append("*Incidents — major (dernière heure)*"); lines.extend(sorted(out_lines)[:10])
    if args.jobs>0:
        th=now-timedelta(hours=args.jobs); job_lines=[]
        for p in Path("jobs").glob("*.md"):
            fm=read_fm(p)
            if not fm.get("remote",False): continue
            mtime=datetime.fromtimestamp(p.stat().st_mtime,tz=timezone.utc)
            if mtime<th: continue
            url=link_to(SITE,"jobs",p.stem)
            job_lines.append(f"• 💼 {fm.get('title','')} @ {fm.get('company','Unknown')} → {url}")
        if job_lines: lines.append("*Jobs remote (dernières 24h)*"); lines.extend(job_lines[:10])
    if not lines: print("No alerts."); return
    msg="\n".join(lines)
    if SLACK: print("Slack:",post_slack(SLACK,msg).status_code)
    if DISCORD: print("Discord:",post_discord(DISCORD,msg).status_code)
    if not SLACK and not DISCORD: print("Preview:\n",msg)

if __name__=="__main__": main()
