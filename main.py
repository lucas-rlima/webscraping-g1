import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://g1.globo.com/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all(class_="bastian-feed-item")


def get_text(classe):
    campo = post.find(class_=classe)
    if campo is None:
        return None
    return campo.text


all_news = []
for post in posts:
    title = get_text("_evt")
    subtitle = get_text("bstn-relatedtext")
    place = get_text("feed-post-metadata-section")
    all_news.append({
        'title': title,
        'subtitle': subtitle,
        'place': place
    })
with open('news.json', 'w') as json_file:
    json.dump(all_news, json_file, indent=3, ensure_ascii=False)