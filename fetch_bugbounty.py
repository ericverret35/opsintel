import requests
from pathlib import Path
from datetime import datetime,timezone
import yaml

OUT_DIR=Path("bugbounty"); OUT_DIR.mkdir(parents=True,exist_ok=True)

def slugify(s): return s.lower().replace(" ","-").replace("/","-").replace(".","-")[:60]

def write_program(prog):
    name=prog.get("name","") or prog.get("program_name",""); url=prog.get("url","") or""
    bounty=prog.get("bounty",False); max_reward=prog.get("max_reward",""); scope=prog.get("scope",[])
    today=datetime.now(timezone.utc).strftime("%Y-%m-%d"); fname=f"{today}-{slugify(name)}.md"; path=OUT_DIR/fname
    if path.exists(): return False
    scope_text="\n".join([f"- {s.get('target',s) if isinstance(s,dict) else s}" for s in (scope or[])[:10]])
    fm={"layout":"post","title":f"{name} — {'💰 Bounty' if bounty else '🆓 No Bounty'}","date":today,"category":"bugbounty","bounty":bounty,"max_reward":max_reward,"url":url,"tags":["bugbounty","security"]}
    content=f"## {name}\n\n**Bounty**: {'Oui' if bounty else 'Non'} {str(max_reward) if max_reward else ''}\n\n### Scope\n\n{scope_text or '_Aucune information_'}\n\n**Programme**: [Inscription]({url})\n"
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n"); f.write(content)
    return True

def fetch_programs():
    try:
        r=requests.get("https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/main/bugbounty-programs.json",timeout=30)
        if r.status_code==200: return r.json().get("programs",[])
    except: pass
    return []

def main():
    print(">> Fetching Bug Bounty programs..."); programs=fetch_programs(); created=0
    for prog in programs[:30]:
        if write_program(prog): created+=1
    print(f"Bug bounty programs: {created}")

if __name__=="__main__": main()
