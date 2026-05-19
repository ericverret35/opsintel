import re,requests
from pathlib import Path
from datetime import datetime,timezone
import yaml

OUT_DIR=Path("k8s_releases"); OUT_DIR.mkdir(parents=True,exist_ok=True)
REPOS=[
  {"org":"kubernetes","repo":"kubernetes","name":"Kubernetes"},
  {"org":"helm","repo":"helm","name":"Helm"},
  {"org":"argoproj","repo":"argo-cd","name":"ArgoCD"},
  {"org":"istio","repo":"istio","name":"Istio"},
  {"org":"prometheus","repo":"prometheus","name":"Prometheus"},
  {"org":"grafana","repo":"grafana","name":"Grafana"},
  {"org":"fluxcd","repo":"flux2","name":"FluxCD"},
  {"org":"crossplane","repo":"crossplane","name":"Crossplane"},
  {"org":"traefik","repo":"traefik","name":"Traefik"},
]

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:80]

def write_release(rel,tool):
    tag=rel.get("tag_name",""); name=rel.get("name","") or tag; body=rel.get("body","") or""
    url=rel.get("html_url",""); prerelease=rel.get("prerelease",False)
    today=datetime.now(timezone.utc).strftime("%Y-%m-%d"); fname=f"{today}-{slugify(tool)}-{slugify(tag)}.md"; path=OUT_DIR/fname
    if path.exists(): return False
    fm={"layout":"post","title":f"{tool} {tag}","date":today,"category":"k8s-releases","tool":tool,"version":tag,"prerelease":prerelease,"url":url,"tags":["kubernetes","cncf",tool.lower()]}
    content=f"## {tool} {tag}\n\n**Version**: {tag}\n**Type**: {'Pre-release' if prerelease else 'Stable'}\n**Release**: [{url}]({url})\n\n### Changelog\n\n{re.sub(r'<[^>]+>',' ',body)[:800]}\n"
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n"); f.write(content)
    return True

def fetch_releases(org,repo):
    try:
        r=requests.get(f"https://api.github.com/repos/{org}/{repo}/releases",headers={"Accept":"application/vnd.github.v3+json"},timeout=20)
        if r.status_code==200: return r.json()[:3]
    except: pass
    return []

def main():
    print(">> Fetching K8s/CNCF releases..."); created=0
    for item in REPOS:
        releases=fetch_releases(item["org"],item["repo"])
        for rel in releases:
            if write_release(rel,item["name"]): created+=1
    print(f"K8s releases posts: {created}")

if __name__=="__main__": main()
