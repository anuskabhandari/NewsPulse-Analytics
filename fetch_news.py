import requests

def fetch_news(limit=20):
    ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ids = requests.get(ids_url).json()

    articles = []

    for i in ids[:limit]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
        data = requests.get(url).json()

        if data:
            articles.append(data)

    return articles


if __name__ == "__main__":
    print(fetch_news()[:2])