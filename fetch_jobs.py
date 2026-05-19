import re,requests,feedparser
from pathlib import Path
from datetime import datetime,timezone
import yaml

OUT_DIR=Path("jobs"); OUT_DIR.mkdir(parents=True,exist_ok=True)
SOURCES=[
  {"name":"Remotive","url":"https://remotive.com/remote-jobs/feed?category=software-dev"},
  {"name":"WeWorkRemotely","url":"https://weworkremotely.com/categories/remote-programming-jobs.rss"},
  {"name":"RemoteOK","url":"https://remoteok.com/feed"},
]
KEYWORDS=["python","golang","go","rust","typescript","javascript","kubernetes","k8s","devops","sre","cloud","aws","gcp","azure","terraform","ansible","linux","security","data","ml","ai","backend","frontend","docker","database","api","graphql","microservices"]
REMOTE_KW=["remote","anywhere","worldwide","europe","usa","global","distributed"]

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:80]
def clean_html(t): return re.sub(r"<[^>]+>"," ",t or"").strip()
def is_relevant(t,d=""): return any(k in (t+" "+d).lower() for k in KEYWORDS)
def is_remote(t,d=""): return any(k in (t+" "+d).lower() for k in REMOTE_KW)

def write_job(job,src):
    title=(job.get("title","") or"").strip(); company=(job.get("company","") or job.get("author","") or"Unknown").strip()
    url=(job.get("url","") or job.get("link","") or"").strip()
    desc=clean_html(job.get("description","") or job.get("summary","") or"")
    if not is_relevant(title,desc): return False
    remote=is_remote(title,desc); tags=[k for k in KEYWORDS if k in (title+desc).lower()][:8]
    date=job.get("date","")[:10] if job.get("date") else datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fname=f"{date}-{slugify(company)}-{slugify(title[:30])}.md"; path=OUT_DIR/fname
    if path.exists(): return False
    fm={"layout":"post","title":f"{title} @ {company}"+(" 🏠 Remote" if remote else ""),"date":date,"category":"jobs","company":company,"url":url,"remote":remote,"tags":["jobs","remote" if remote else "onsite",src.lower()]+tags}
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write(f"## {title}\n\n**Entreprise**: {company}\n**Remote**: {'Oui 🏠' if remote else 'Non'}\n**Source**: {src}\n\n### Description\n\n{desc[:800] or '_Pas de description_'}\n\n👉 [Voir l'offre]({url})\n")

def fetch_all(url,src):
    jobs=[]; feed=feedparser.parse(url)
    for e in feed.entries[:20]:
        job={"title":e.get("title",""),"company":e.get("author","") or e.get("publisher",""),"url":e.get("link",""),"description":e.get("summary",""),"date":e.get("published","")}
        jobs.append(job)
    return jobs

def main():
    print(">> Fetching Dev Jobs..."); created=0
    for src in SOURCES:
        try: jobs=fetch_all(src["url"],src["name"]); [write_job(j,src["name"]) and __import__('sys').stdout.write('.') or None for j in jobs]; print(f"\n{src['name']}: {len(jobs)} fetched")
        except Exception as e: print(f"\nError {src['name']}: {e}")
    print(f"Jobs posts created: {created}")

if __name__=="__main__": main()
