import requests
from bs4 import BeautifulSoup
import os

url = "https://catalog.morgan.edu/preview_program.php?catoid=26&poid=5968&returnto=1888"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

os.makedirs("data", exist_ok=True)

with open("data/morgan_cs_catalog.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Catalog saved.")
print("Characters scraped:", len(text))