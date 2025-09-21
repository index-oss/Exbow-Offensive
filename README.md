# EXBOW‑lite Autonomous Bug‑Hunting Tool

## 🚀 Quickstart (GitHub Codespaces)

1. Clone this repo and click **Code → Open in Codespaces**
2. Add your API keys by copying `.env.example` to `.env`
3. Codespace setup runs automatically


## 🛠️ Example flow

```bash
python recon/scan.py example.com
python ai/analyze.py
python exploit/exploit.py
```

Reports are generated in the `reports/` folder for review.
python recon/scan.py example.com
python ai/analyze.py
python exploit/exploit.py
markdown-pdf reports/report_template.md -o reports/latest_report.pdf
git add .
git commit -m "Initial working version"
git push origin main





# EXBOW-Lite: Autonomous AI-Powered Bug Hunting System

## ✅ Project Summary

**Goal:** Build a modular AI system that automates the bug bounty kill-chain:  

**Recon → AI Analysis → Exploitation → Reporting**  

**Outcome:** A local or cloud-based tool that autonomously finds and reports real bugs using LLM/AI assistance.

---

## 🧩 Phase Roadmap

| Phase | Description |
|-------|-------------|
| 0 🔐 Config & Setup | Install tools, get keys, setup environment, configure AI stack |
| 1 📡 Recon Engine | Asset discovery + tagging using tools + AI-based classification |
| 2 🧠 AI Vuln Analyzer | Use LLM to predict potential vulnerabilities from recon data |
| 3 💣 Exploit Generator | Auto-generate and test PoCs using Python, curl, SQLmap, or Selenium |
| 4 📝 Auto Reporting Engine | Generate reports with CVSS calculation; export Markdown → PDF |
| 5 🔄 Automation & Pipelines | Loop full chain using Cron or Apache Airflow |

---

## ⏱ Estimated Time

| Phase | Time (1 Dev, Focused) |
|-------|----------------------|
| Setup & Config | 1–2 days |
| Recon Engine | 1–2 days |
| AI Analyzer | 2–4 days |
| Exploit Generator | 3–5 days |
| Reporting Engine | 2–3 days |
| Pipeline Automation | 2 days |
| **Total** | 11–18 days |

---

## ⚙️ Tech Stack

### 🧠 AI / LLM
| Tool | Role | Notes |
|------|------|------|
| Groq API | LLM backend | Free, optional |
| LLaMA 3 / DeepSeek | Local AI runtime | For offline use |
| OpenAI GPT-4o | Optional premium | Backup LLM |

### 🔍 Recon
| Tool | Role |
|------|------|
| subfinder | Subdomain discovery |
| httpx | Live host detection |
| nuclei | Template-based vulnerability scanning |
| dirsearch | Directory brute force discovery |

### 💣 Exploit
| Tool | Role |
|------|------|
| Python Scripts | PoC generation & validation |
| curl / sqlmap | Automated exploitation |
| Selenium | Browser automation |

### 📝 Reporting
| Tool | Role |
|------|------|
| Markdown | Human-readable report |
| Pandoc / PDF | Export reports to PDF |
| GitHub CLI | Optional push reports to repo |

---

## 🔐 Accounts & Key Config

| Tool | Config Needed | How to Get |
|------|---------------|------------|
| Groq API | API Key | [Groq Console](https://console.groq.com) |
| OpenAI GPT | `OPENAI_API_KEY` | [OpenAI Platform](https://platform.openai.com/) |
| GitHub | `GITHUB_TOKEN` (optional) | Developer Settings → Tokens |
| Nuclei | None | CLI install |
| Subfinder | None | CLI install |

**Recommended `.env` file structure:**
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxx


---

##🚀 First Launch Plan

###1️⃣ Install Base Tools

brew install subfinder httpx nuclei dirsearch
pip install selenium requests python-dotenv

2️⃣ Install LLM Tools

Groq API:

1. Create free account: https://console.groq.com


2. Copy your API key



Ollama (Local LLM):

curl -fsSL https://ollama.com/install.sh | sh
ollama run deepseek-coder:33b

3️⃣ Clone Repository

git clone <REPO_URL>
cd <REPO_NAME>

4️⃣ Setup Environment

Create .env in the root directory with API keys

Ensure Python dependencies installed (pip install -r requirements.txt)


5️⃣ Run Initial Recon Test

python recon_bot.py -d hackerone.com

6️⃣ Review Results

live.txt → Live hosts discovered

nuclei-findings.txt → Vulnerabilities found

classified.txt → Assets classified by AI


✅ System ready for integration with AI Analyzer, Exploit Generator, and Reporting Engine.


---

🔧 Notes

Ensure your .env is never pushed to public repos

Start with small, legal targets (like your own lab or authorized bug bounty targets)

All modules are modular, so you can test each phase independently



---

📌 Future Modules

AI Vulnerability Analyzer → LLM-based prediction & prioritization

Exploit Generator → Auto-PoC & validation

Auto-Reporting → Markdown → PDF + CVSS scoring

Pipeline Automation → Cron or Airflow for full chain execution



---

🧠 Learning & Contribution

Read the docs for each tool (subfinder, nuclei, dirsearch)

Familiarize with OpenAI / Groq APIs for AI integration

Contribute to modules independently — modular design ensures easy scaling


---

I can also create a **fully functional `recon_bot.py`** next with:

- Subdomain scanning (`subfinder`)  
- Live host detection (`httpx`)  
- Nuclei vulnerability scanning  
- Smart AI classification + Groq/OpenAI prompt builder  
