import os,re,time,requests
from pathlib import Path
from datetime import datetime,timedelta,timezone
from dateutil import tz
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import yaml

NVD_URL="https://services.nvd.nist.gov/rest/json/cves/2.0"
OUT_DIR=Path("cve"); TZ_UTC=tz.gettz("UTC")

def iso(dtobj): return dtobj.replace(tzinfo=TZ_UTC).isoformat().replace("+00:00","Z")

def fetch_cves(start,end,api_key=None):
    params={"lastModStartDate":iso(start),"lastModEndDate":iso(end),"startIndex":0,"resultsPerPage":2000}
    headers={}
    if api_key: headers["apiKey"]=api_key
    all_items=[]
    while True:
        r=requests.get(NVD_URL,params=params,headers=headers,timeout=60); r.raise_for_status()
        data=r.json(); items=data.get("vulnerabilities",[]); all_items.extend(items)
        total=data.get("totalResults",len(all_items)); params["startIndex"]+=len(items)
        if params["startIndex"]>=total or not items: break
        time.sleep(0.6)
    return [i["cve"] for i in all_items]

def get_cvss_metrics(cve):
    m=cve.get("metrics",{})
    for key in ("cvssMetricV31","cvssMetricV30","cvssMetricV2"):
        if key in m and m[key]:
            d=m[key][0].get("cvssData",{}); sev=m[key][0].get("baseSeverity","") or d.get("baseSeverity","")
            return sev,d.get("baseScore",None),d.get("vectorString","")
    return "",None,""

def extract_cwe(cve):
    ws=cve.get("weaknesses",[])
    if ws and "description" in ws[0] and ws[0]["description"]: return ws[0]["description"][0].get("value","")
    return ""

def extract_refs(cve,limit=5): return [r.get("url") for r in cve.get("references",[])[:limit] if r.get("url")]

def extract_vendors_products(cve,limit=5):
    vendors,products=set(),set()
    for conf in cve.get("configurations",[]):
        for node in conf.get("nodes",[]):
            for match in node.get("cpeMatch",[]):
                uri=match.get("criteria") or match.get("cpe23Uri")
                if uri and uri.startswith("cpe:2.3:"):
                    parts=uri.split(":"); 
                    if len(parts)>5:
                        v=parts[3];p=parts[4]
                        if v!="*": vendors.add(v)
                        if p!="*": products.add(p)
    return list(vendors)[:limit],list(products)[:limit]

def lexrank_summary(text,sentences=2):
    text=re.sub(r"\s+"," ",(text or "").strip())
    if not text: return ""
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
    sents=LexRankSummarizer()(parser.document,sentences)
    return " ".join(str(s) for s in sents) or text[:300]

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or "").lower()).strip("-")

def write_post(cve):
    cve_id=cve.get("id"); descs=cve.get("descriptions",[]); desc=""
    for d in descs:
        if d.get("lang","en").lower()=="en": desc=d.get("value",""); break
    if not desc and descs: desc=descs[0].get("value","")
    sev,score,vector=get_cvss_metrics(cve); cwe=extract_cwe(cve); refs=extract_refs(cve)
    vendors,products=extract_vendors_products(cve)
    title=f"{cve_id} — {sev or 'UNSPEC'}"; summary=lexrank_summary(desc,2)
    pub=cve.get("published") or cve.get("lastModified") or datetime.utcnow().isoformat(); date=pub[:10]
    tags=[]
    if sev: tags.append(sev.lower())
    if cwe: tags.append(slugify(cwe)[:30])
    if vendors: tags.extend([slugify(v) for v in vendors[:3]])
    fm={"layout":"post","title":title,"date":date,"categories":["cve"],"tags":tags[:6],"severity":sev,"cvss":score,"vector":vector,"cwe":cwe,"vendors":vendors,"products":products,"links":refs}
    OUT_DIR.mkdir(parents=True,exist_ok=True)
    path=OUT_DIR/f"{date}-{slugify(cve_id)}.md"
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write(summary+"\n\n## Details\n\n"+(desc or"")+"\n\n")
        if refs: f.write("## References\n\n"+"".join(f"- {u}\n" for u in refs))

def main():
    api_key=os.getenv("NVD_API_KEY")
    end=datetime.now(timezone.utc); start=end-timedelta(days=1)
    cves=fetch_cves(start,end,api_key)
    if not cves: print("No new CVEs."); return
    for cve in cves: write_post(cve)
    print(f"Wrote {len(cves)} CVE posts.")

if __name__=="__main__": main()
