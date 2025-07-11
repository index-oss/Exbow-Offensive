import subprocess
import sys

def run(cmd, outfile=None):
    print(f"→ Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if outfile:
        with open(outfile, "w") as f:
            f.write(result.stdout)
    return result.stdout

def main(domain):
    subs = run(f"subfinder -d {domain} -silent", "recon/subs.txt")
    live = run(f"httpx -l recon/subs.txt -silent -title -tech-detect", "recon/live.txt")
    find = run(f"nuclei -l recon/live.txt -o recon/findings.txt", "recon/findings.txt")
    print("Recon complete!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scan.py <domain>")
    else:
        main(sys.argv[1])