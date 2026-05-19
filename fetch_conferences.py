from pathlib import Path
from datetime import datetime,timezone
import yaml

OUT_DIR=Path("conferences"); OUT_DIR.mkdir(parents=True,exist_ok=True)

CONFS=[
  {"name":"KubeCon North America 2025","date":"2025-11-10","location":"Atlanta, USA","url":"https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/","cfp":"2025-03-15"},
  {"name":"KubeCon Europe 2025","date":"2025-04-01","location":"London, UK","url":"https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/","cfp":"2024-12-15"},
  {"name":"PyCon US 2025","date":"2025-05-14","location":"Pittsburgh, USA","url":"https://us.pycon.org/2025/","cfp":"2025-01-20"},
  {"name":"DEF CON 33","date":"2025-08-07","location":"Las Vegas, USA","url":"https://defcon.org/","cfp":"2025-04-01"},
  {"name":"Black Hat USA 2025","date":"2025-08-02","location":"Las Vegas, USA","url":"https://www.blackhat.com/","cfp":"2025-04-15"},
  {"name":"RSA Conference 2025","date":"2025-04-28","location":"San Francisco, USA","url":"https://www.rsaconference.com/","cfp":"2024-11-01"},
  {"name":"AWS re:Invent 2025","date":"2025-12-01","location":"Las Vegas, USA","url":"https://reinvent.awsevents.com/","cfp":"2025-06-01"},
  {"name":"GopherCon 2025","date":"2025-09-15","location":"Denver, USA","url":"https://www.gophercon.com/","cfp":"2025-04-01"},
  {"name":"RustConf 2025","date":"2025-08-20","location":"Seattle, USA","url":"https://rustconf.com/","cfp":"2025-05-01"},
  {"name":"NodeConf 2025","date":"2025-06-12","location":"Dublin, Ireland","url":"https://www.nodeconf.com/","cfp":"2025-02-01"},
]

def slugify(s): return s.lower().replace(" ","-").replace("/","-")[:60]

def write_conf(conf):
    name=conf.get("name",""); date=conf.get("date",""); location=conf.get("location",""); url=conf.get("url",""); cfp=conf.get("cfp","")
    today=datetime.now(timezone.utc).strftime("%Y-%m-%d"); fname=f"{date}-{slugify(name)}.md"; path=OUT_DIR/fname
    if path.exists(): return False
    fm={"layout":"post","title":f"📅 {name}","date":today,"category":"conferences","conference":name,"location":location,"cfp_deadline":cfp,"url":url,"tags":["conferences","events"]}
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n")
        f.write(f"## {name}\n\n**Lieu**: {location}\n**Date**: {date}\n**CFP**: {cfp or 'Non spécifié'}\n\n**En savoir plus**: [Site]({url})\n")
    return True

def main():
    print(">> Fetching Conferences..."); created=0
    for conf in CONFS:
        if write_conf(conf): created+=1
    print(f"Conference posts: {created}")

if __name__=="__main__": main()
