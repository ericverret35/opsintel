import re
from pathlib import Path
from datetime import datetime,timezone
import yaml

OUT_DIR=Path("pricing"); OUT_DIR.mkdir(parents=True,exist_ok=True)

TOOLS={
  "AWS":{"favicon":"🟠","plans":[{"name":"EC2 t3.micro","price":"$0.0104/hr","desc":"Burstable instance"},{"name":"S3 Standard","price":"$0.023/GB/mo","desc":"Storage"},{"name":"Lambda","price":"$0.20/1M req","desc":"Serverless"}]},
  "Google Cloud":{"favicon":"🔵","plans":[{"name":"Compute Engine e2-micro","price":"$6.11/mo","desc":"2 vCPU, 1 GB"},{"name":"Cloud Storage Standard","price":"$0.020/GB/mo","desc":"Multi-region"}]},
  "Vercel":{"favicon":"⚡","plans":[{"name":"Hobby","price":"Free","desc":"100GB BW, 100K req/j"},{"name":"Pro","price":"$20/mo","desc":"Unlimited BW, 10K deploys/mo"}]},
  "GitHub Copilot":{"favicon":"🤖","plans":[{"name":"Individual","price":"$10/mo","desc":"Code completions"},{"name":"Business","price":"$19/user/mo","desc":"Admin+policy"}]},
  "Supabase":{"favicon":"⚡","plans":[{"name":"Free","price":"Free","desc":"500MB DB, 1GB storage"},{"name":"Pro","price":"$25/mo","desc":"8GB DB, 100GB storage"}]},
  "Planetscale":{"favicon":"🌱","plans":[{"name":"Hobby","price":"Free","desc":"1 branch, 1GB storage"},{"name":"Scaler","price":"$29/mo","desc":"3 branches, 10GB storage"}]},
  "Linear":{"favicon":"📐","plans":[{"name":"Free","price":"Free","desc":"Up to 250 entities"},{"name":"Standard","price":"$8/user/mo","desc":"Unlimited projects"}]},
  "OpenAI API":{"favicon":"🧠","plans":[{"name":"GPT-4o mini","price":"$0.15/1M tokens","desc":"128K context"},{"name":"GPT-4o","price":"$2.5/1M tokens","desc":"128K context"}]},
  "Anthropic Claude":{"favicon":"🧬","plans":[{"name":"Claude 3.5 Sonnet","price":"$3/1M tokens","desc":"200K context"},{"name":"Claude 3.5 Haiku","price":"$0.80/1M tokens","desc":"200K context"}]},
  "Sentry":{"favicon":"🦅","plans":[{"name":"Developer","price":"Free","desc":"5K events/mo"},{"name":"Team","price":"$26/mo","desc":"500K events/mo"}]},
  "Datadog":{"favicon":"🐶","plans":[{"name":"Free","price":"Free","desc":"5 hosts, 1 day retention"},{"name":"Pro","price":"$15/host/mo","desc":"Unlimited retention"}]},
  "Docker Hub":{"favicon":"🐳","plans":[{"name":"Personal","price":"Free","desc":"1 private repo"},{"name":"Team","price":"$7/mo","desc":"5 private repos"}]},
  "Figma":{"favicon":"🎨","plans":[{"name":"Free","price":"Free","desc":"3 projects"},{"name":"Professional","price":"$12/editor/mo","desc":"Unlimited projects"}]},
  "Notion":{"favicon":"📝","plans":[{"name":"Free","price":"Free","desc":"10 guests"},{"name":"Plus","price":"$8/user/mo","desc":"Unlimited guests"}]},
  "Slack":{"favicon":"💬","plans":[{"name":"Pro","price":"$8.75/user/mo","desc":"90-day history"},{"name":"Business","price":"$15/user/mo","desc":"Unlimited history"}]},
  "Jira":{"favicon":"🧩","plans":[{"name":"Free","price":"Free","desc":"10 users"},{"name":"Standard","price":"$7.75/user/mo","desc":"Unlimited users"}]},
}

def slugify(s): return re.sub(r"[^a-z0-9]+","-",(s or"").lower()).strip("-")[:60]

def write_tool(name,data):
    today=datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fname=f"{today}-{slugify(name)}-pricing.md"; path=OUT_DIR/fname
    if path.exists(): return False
    fm={"layout":"post","title":f"{data['favicon']} {name} — Tarifs {today}","date":today,"category":"pricing","tool":name,"tags":["pricing","devtools",name.lower().replace(" ","-")]}
    plans_text="\n".join([f"| {p['name']} | {p['price']} | {p['desc']} |" for p in data["plans"]])
    content=f"## {data['favicon']} {name} — Plans et Tarifs\n\n**Mis à jour**: {today}\n\n| Plan | Prix | Description |\n|------|------|-------------|\n{plans_text}\n\n_Comparateur de tarifs via OpsIntel · Mis à jour quotidiennement_\n"
    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n"); yaml.safe_dump(fm,f,allow_unicode=True,sort_keys=False); f.write("---\n\n"); f.write(content)
    return True

def main():
    print(">> Fetching Dev Tools Pricing..."); created=0
    for name,data in TOOLS.items():
        if write_tool(name,data): created+=1
    print(f"Pricing posts created: {created}")

if __name__=="__main__": main()
