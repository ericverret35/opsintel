import json,requests,re
from pathlib import Path
from datetime import datetime,timezone
import yaml

OUT_DIR=Path("github_trending"); OUT_DIR.mkdir(parents=True,exist_ok=True)
BASE="https://api.github.com"; LANGS=["python","javascript","go","rust","typescript","java","c"]

def slugify(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")

def write_repo(repo):
    name=repo.get("name",""); full_name=repo.get("full_name",""); desc=repo.get("description") or "No description"
    stars=repo.get("stargazers_count",0); forks=repo.get("forks_count",0); lang=repo.get("language") or "Unknown"
    url=repo.get("html_url",""); topics=repo.get("topics",[])[:10]
    today=datetime.now(timezone.utc).strftime("%Y-%m-%d"); fname=f"{today}-{slugify(name)}.md"; path=OUT_DIR/fname
    if path.exists(): return False
    fm={"layout":"post","title":f"{name} ⭐ {stars:,}","date":today,"category":"github-trending","stars":stars,"forks":forks,"language":lang,"topics":topics,"url":url,"tags":["github-trending",lang.lower() if lang else"unknown"]+topics[:3]}
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write(f"## {full_name}\n\n**Description**: {desc}\n\n**Stats**: ⭐ {stars:,} | 🍴 {forks:,} | 🏷️ {lang}\n\n**Topics**: {', '.join(topics) if topics else 'None'}\n\n**Repo**: [GitHub]({url})\n")
    return True

def fetch_trending(lang=None):
    try:
        days_ago=(datetime.now(timezone.utc)-datetime(2024,1,1,tzinfo=timezone.utc)).days
        params={"q":f"created:>{datetime.now().strftime('%Y-%m-%d')}" if not lang else f"language:{lang} created:>{datetime.now().strftime('%Y-%m-%d')}","sort":"stars","order":"desc","per_page":10}
        r=requests.get(f"{BASE}/search/repositories",params=params,timeout=30); r.raise_for_status()
        return r.json().get("items",[])
    except: return []

def main():
    print(">> Fetching GitHub Trending..."); created=0
    for lang in LANGS:
        repos=fetch_trending(lang)
        for repo in repos:
            if write_repo(repo): created+=1
    print(f"GitHub Trending posts: {created}")

if __name__=="__main__": main()
