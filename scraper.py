import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".titleline a")

print("📰 Güncel Başlıklar:\n")

for idx, title in enumerate(titles[:10], start=1):
    print(f"{idx}. {title.text}")
