import requests
import json

query = input("what's your intrest in news: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-27&sortBy=publishedAt&apiKey=041623a956764982b4bb1f25d7cc5d3e"

r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------------------------")