import re,feedparser
from pathlib import Path
from datetime import datetime,timedelta,timezone
from time import mktime
import yaml

OUT_DIR=Path("podcasts"); OUT_DIR.mkdir(parents=True,exist_ok=True)
SOURCES=[{"name":"Risky Business","url":"https://risky.biz/feed/mp3"},{"name":"Darknet Diaries","url":"https://feeds.megaphone.fm/darknetdiaries"}]

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:60]

def write_episode(src,entry):
    title=(entry.get("title","") or"").strip(); link=entry.get("link","") or entry.get("id","")
    summary=re.sub(r"<[^>]+>"," ",(entry.get("summary","") or entry.get("description","") or"").strip())[:500]
    published=entry.get("published_parsed") or entry.get("updated_parsed")
    if published:
        try: dt=datetime.fromtimestamp(mktime(published),tz=timezone.utc); date=dt.strftime("%Y-%m-%d")
        except: date=datetime.now(timezone.utc).strftime("%Y-%m-%d")
    else: date=datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fname=f"{date}-{slugify(src)}-{slugify(title[:40])}.md"; path=OUT_DIR/fname
    if path.exists(): return False
    fm={"layout":"post","title":title,"date":date,"category":"podcasts","source":src,"url":link,"tags":["podcasts","security",src.lower()]}
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write(f"## {title}\n\n**Podcast**: {src}\n\n{summary}\n\n**Écouter**: [Lien]({link})\n")
    return True

def main():
    print(">> Fetching Security Podcasts..."); now=datetime.now(timezone.utc); cutoff=now-timedelta(days=3); created=0
    for src in SOURCES:
        try:
            feed=feedparser.parse(src["url"])
            for e in feed.entries[:5]:
                p=e.get("published_parsed") or e.get("updated_parsed")
                if p:
                    try: dt=datetime.fromtimestamp(mktime(p),tz=timezone.utc)
                    except: continue
                    if dt>=cutoff and write_episode(src["name"],e): created+=1
        except Exception as e: print(f"Error {src['name']}: {e}")
    print(f"Podcast episodes: {created}")

if __name__=="__main__": main()
