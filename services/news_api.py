import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news():
    params = {
        "country": "mx",
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()["articles"]