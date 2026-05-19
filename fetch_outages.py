import re,calendar
from pathlib import Path
from datetime import datetime,timedelta,timezone
import feedparser,yaml

OUT_DIR=Path("outages")
SOURCES=[
  {"name":"GitHub","url":"https://www.githubstatus.com/history.atom"},
  {"name":"Cloudflare","url":"https://www.cloudflarestatus.com/history.atom"},
  {"name":"Slack","url":"https://status.slack.com/feed/atom"},
  {"name":"Google Cloud","url":"https://status.cloud.google.com/feed.atom"},
  {"name":"Stripe","url":"https://status.stripe.com/history.atom"},
  {"name":"OpenAI","url":"https://status.openai.com/history.atom"},
  {"name":"Discord","url":"https://discordstatus.com/history.atom"},
  {"name":"Vercel","url":"https://www.vercel-status.com/history.atom"},
  {"name":"Supabase","url":"https://status.supabase.com/history.atom"},
  {"name":"Datadog","url":"https://status.datadoghq.com/history.atom"},
  {"name":"Twilio","url":"https://status.twilio.com/history.atom"},
  {"name":"Sentry","url":"https://status.sentry.io/history.atom"},
  {"name":"Algolia","url":"https://status.algolia.com/history.atom"},
  {"name":"Auth0","url":"https://status.auth0.com/history.atom"},
  {"name":"Okta","url":"https://status.okta.com/history.atom"},
]
LOOKBACK_HOURS=2

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:80]
def classify(title,summary=""):
    t=(title+" "+summary).lower()
    if "major" in t or "outage" in t: return "major"
    if "partial" in t or "degraded" in t: return "partial"
    if "resolved" in t: return "resolved"
    return "incident"
def to_utc(ts): return datetime.fromtimestamp(calendar.timegm(ts),tz=timezone.utc)

def write_post(vendor,entry):
    title=(entry.get("title","") or"").strip(); link=entry.get("link",""); summary=(entry.get("summary","") or"").strip()
    published=entry.get("published_parsed") or entry.get("updated_parsed")
    if not published: return
    dtobj=to_utc(published); date=dtobj.strftime("%Y-%m-%d"); sev=classify(title,summary)
    fname=f"{date}-{slugify(vendor)}-{slugify(title)}.md"; path=OUT_DIR/fname
    if path.exists(): return
    fm={"layout":"post","title":title,"date":date,"vendor":vendor,"severity":sev,"link":link,"tags":[vendor.lower(),sev]}
    OUT_DIR.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write((summary[:2000] or "Update")+"\n\n")
        if link: f.write(f"More details: {link}\n")

def main():
    now=datetime.now(tz=timezone.utc); cutoff=now-timedelta(hours=LOOKBACK_HOURS)
    for src in SOURCES:
        feed=feedparser.parse(src["url"])
        if getattr(feed,"bozo",0) and not getattr(feed,"entries",None): continue
        for e in feed.entries:
            ts=e.get("published_parsed") or e.get("updated_parsed")
            if not ts: continue
            dtobj=to_utc(ts)
            if dtobj>=cutoff: write_post(src["name"],e)

if __name__=="__main__": main()
