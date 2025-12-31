import requests
from config import NEWS_API_KEY

def fetch_articles():
    if not NEWS_API_KEY or not NEWS_API_KEY.strip():
        raise RuntimeError("NEWS_API_KEY is missing. Set it in your environment or .env.")

    api_key = NEWS_API_KEY.strip()
    url = "https://newsapi.org/v2/everything"
    headers = {"X-Api-Key": api_key}
    params = {
        "q": "artificial intelligence OR technology",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    articles = response.json()["articles"]
    return articles  

