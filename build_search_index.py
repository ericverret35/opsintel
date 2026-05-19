import os,re,json,yaml
from pathlib import Path

OUT=Path("assets"); OUT.mkdir(exist_ok=True); BASE=os.getenv("SITE_BASE_URL","").rstrip("/")

def read_post(path):
    raw=path.read_text(encoding="utf-8")
    if not raw.startswith("---"): return {},""
    fm_txt=raw.split("---",2)[1]; body=raw.split("---",2)[2]
    fm=yaml.safe_load(fm_txt) or {}; text=re.sub(r"<[^>]+>"," ",body); text=re.sub(r"\s+"," ",text).strip()
    return fm,text[:800]

def collect(coll,base):
    docs=[]
    for p in Path(base).glob("*.md"):
        fm,text=read_post(p)
        url=f"{BASE}/{coll}/{p.stem}/" if BASE else f"/{coll}/{p.stem}/"
        docs.append({"id":f"{coll}:{p.stem}","title":fm.get("title",""),"url":url,"tags":fm.get("tags") or [],"content":text})
    return docs

def main():
    docs=[]
    for coll,base in [("cve","cve"),("outages","outages"),("ai","papers"),("advisories","advisories"),("github","github_trending"),("news","tech_news"),("jobs","jobs"),("k8s","k8s_releases"),("bugbounty","bugbounty"),("podcasts","podcasts"),("pricing","pricing"),("ctf","ctf"),("conf","conferences")]:
        docs+=collect(coll,base)
    Path("assets/search.json").write_text(json.dumps(docs,ensure_ascii=False),encoding="utf-8")
    print("search.json written:",len(docs))

if __name__=="__main__": main()
