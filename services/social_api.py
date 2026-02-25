import requests

BASE_URL = "https://dummyjson.com"

def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    return response.json()["posts"]
