import re,calendar
from pathlib import Path
from datetime import datetime,timedelta,timezone
import feedparser,yaml
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

OUT_DIR=Path("papers"); CATEGORIES=["cs.AI","cs.LG","stat.ML"]; MAX_RESULTS=40; LOOKBACK_DAYS=1

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:80]
def summarize(text,n=2):
    text=re.sub(r"\s+"," ",text or"").strip()
    if not text: return ""
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
    sents=LexRankSummarizer()(parser.document,n)
    return " ".join(str(s) for s in sents) or text[:300]
def query_url(cat): return f"http://export.arxiv.org/api/query?search_query=cat:{cat}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={MAX_RESULTS}"

def write_post(entry,cat):
    title=(entry.get("title","") or"").strip(); link=entry.get("link","")
    abstract=(entry.get("summary","") or"").strip(); summary=summarize(abstract,2)
    authors=[a.get("name","") for a in entry.get("authors",[])]
    published=entry.get("published_parsed")
    if not published: return
    dtobj=datetime.fromtimestamp(calendar.timegm(published),tz=timezone.utc); date=dtobj.strftime("%Y-%m-%d")
    slug=slugify(title); path=OUT_DIR/f"{date}-{slug}.md"
    if path.exists(): return
    fm={"layout":"post","title":title,"date":date,"category":"paper","arxiv_category":cat,"authors":authors,"link":link,"tags":["arxiv",cat.replace(".","-")]}
    OUT_DIR.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write(summary+"\n\n## Abstract\n\n"+abstract+"\n\n")
        if link: f.write(f"Source: {link}\n")

def main():
    cutoff=datetime.now(tz=timezone.utc)-timedelta(days=LOOKBACK_DAYS)
    for cat in CATEGORIES:
        feed=feedparser.parse(query_url(cat))
        for e in feed.entries:
            ts=e.get("published_parsed")
            if not ts: continue
            dtobj=datetime.fromtimestamp(calendar.timegm(ts),tz=timezone.utc)
            if dtobj>=cutoff: write_post(e,cat)

if __name__=="__main__": main()
