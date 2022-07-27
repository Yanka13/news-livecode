# client/__init__.py
import requests

BASE_URL = "https://newsapi.org/v2"
API_KEY = "367f28d82c3b42e2bb224b79b0ef480e"
class News:

    def top_headlines(self, country):
        params = {"country": country, "apiKey": API_KEY }
        r = requests.get(f"{BASE_URL}/top-headlines", params=params).json().get("articles", None)
        return r

    def search_keyword(self, keyword):
        params = {"q": keyword, "apiKey": API_KEY}
        r = requests.get(f"{BASE_URL}/everything", params=params).json().get("articles", None)
        return r


