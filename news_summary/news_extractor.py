from dotenv import load_dotenv
import requests
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
URL = "https://newsapi.org/v2/top-headlines?"


def get_articles(category, country):

    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": NEWS_API_KEY
    }
    articles = requests.get(URL, query_parameters).json()
    return articles["articles"]


def filter_articles(articles):
    filtered_articles = []

    for article in articles:
        filtered_articles.append({
            "title": article["title"],
            "description": article["description"],
            "content": article["content"],
        })
    return filtered_articles
