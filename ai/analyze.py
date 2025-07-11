import os, json
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = os.getenv("GROQ_API_URL")

with open("recon/live.txt") as f:
    lines = f.read().splitlines()

prompt = f"""
Target endpoints found:
""" + "\n".join(f"- {l}" for l in lines[:10]) + "\n\nSuggest 3 probable vulnerabilities with example PoC payloads in curl format."

headers = {"Authorization": f"Bearer {API_KEY}"}
payload = {"model":"llama3-70b-8192","messages":[{"role":"user","content":prompt}]}

resp = requests.post(API_URL, json=payload, headers=headers)
resp.raise_for_status()
data = resp.json()
content = data.get("choices", [])[0]["message"]["content"]

with open("ai/ai_output.json", "w") as f:
    json.dump({"prompt": prompt, "response": content}, f, indent=2)

print("AI suggestions saved to ai/ai_output.json")