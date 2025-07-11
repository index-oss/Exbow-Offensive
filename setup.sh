#!/bin/bash
set -e
apt-get update
apt-get install -y curl git python3 python3-pip

# Install subfinder
curl -sL https://github.com/projectdiscovery/subfinder/releases/latest/download/subfinder-linux-amd64 -o /usr/local/bin/subfinder
chmod +x /usr/local/bin/subfinder

# Install httpx
curl -sL https://github.com/projectdiscovery/httpx/releases/latest/download/httpx-linux-amd64 -o /usr/local/bin/httpx
chmod +x /usr/local/bin/httpx

# Install nuclei
curl -sL https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei-linux-amd64 -o /usr/local/bin/nuclei
chmod +x /usr/local/bin/nuclei

# Clone dirsearch
git clone https://github.com/maurosoria/dirsearch.git /opt/dirsearch

pip3 install requests python-dotenv markdown2 markdown-pdf openai
echo "[+] Setup completed."