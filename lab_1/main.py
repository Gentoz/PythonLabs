from bs4 import BeautifulSoup
import requests

try:
    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.read())

except FileNotFoundError:

    for count in range(0, 155):

        url = f"https://www.omgtu.ru/l/?rss=y&PAGEN_1={count}"

        response = requests.get(url)

        if response.ok:

            source = BeautifulSoup(response.content, "lxml")

            data = source.find("div", class_="news")

            newsList = data.find_all("div", class_="news__item")

            with open("file.txt", "a", encoding="utf-8") as f:
                for news in newsList:
                    f.write(news.text)

    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.read())
