from pathlib import Path
import requests
from bs4 import BeautifulSoup

URLS = [
    ("https://www.morgan.edu/computer-science-bs", "computer_science_bs.txt"),
    ("https://www.morgan.edu/computer-science/degrees-and-programs/bs_computerscience", "bs_computerscience.txt"),
]

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)

def scrape_page(url: str, filename: str):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = clean_text(soup.get_text(separator="\n"))
    out_path = OUTPUT_DIR / filename
    out_path.write_text(text, encoding="utf-8")
    print(f"Saved {out_path}")

def main():
    for url, filename in URLS:
        try:
            scrape_page(url, filename)
        except Exception as e:
            print(f"Failed on {url}: {e}")

if __name__ == "__main__":
    main()
