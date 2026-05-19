import re,requests,yaml
from pathlib import Path

CVE_DIR=Path("cve"); KEV_URL="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

def read_post(path):
    txt=path.read_text(encoding="utf-8")
    if not txt.startswith("---"): return None,None
    parts=txt.split("---",2); fm=yaml.safe_load(parts[1]) or {}; body=parts[2]
    return fm,body

def write_post(path,fm,body): path.write_text("---\n"+yaml.safe_dump(fm,allow_unicode=True,sort_keys=False)+"---\n"+body,encoding="utf-8")

def extract_cve_id(fm):
    t=(fm.get("title") or""); m=re.search(r"CVE-\d{4}-\d+",t)
    return m.group(0) if m else None

def main():
    try:
        data=requests.get(KEV_URL,timeout=30).json()
        kev_ids={v.get("cveID") for v in data.get("vulnerabilities",[]) if v.get("cveID")}
    except Exception as e: print("KEV fetch failed:",e); return
    changed=0
    for p in CVE_DIR.glob("*.md"):
        fm,body=read_post(p)
        if fm is None: continue
        cid=extract_cve_id(fm)
        if cid and cid in kev_ids and not fm.get("kev",False): fm["kev"]=True; write_post(p,fm,body); changed+=1
    print(f"KEV flags updated: {changed}")

if __name__=="__main__": main()
