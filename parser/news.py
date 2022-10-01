import requests
from bs4 import BeautifulSoup as BS

URL = "https://www.securitylab.ru/news/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",

}


def get_html(url, params=''):
    reg = requests.get(url=url, headers=HEADERS, params=params)
    return reg


def get_data(html):
    soup = BS(html, "html.parser")
    iteams = soup.find_all("div", class_="article-card-details")


news = []
for news in news:
    news.append({
        "news": ""
    })

html = get_html(URL)
get_data(html.text)
