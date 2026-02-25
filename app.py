from flask import Flask, render_template
from services.social_api import get_posts
from services.weather_api import get_weather
from services.news_api import get_news

app = Flask(__name__)

@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/weather")
def weather():
    weather_data = get_weather()
    return render_template("weather.html", weather=weather_data)

@app.route("/news")
def news():
    news_data = get_news()
    return render_template("news.html", news=news_data)

if __name__ == "__main__":
    app.run(debug=True)