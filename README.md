# XBOW‑lite Autonomous Bug‑Hunting Tool

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
