from chalice import Chalice
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
app = Chalice(app_name='daily-news')

@app.route('/news')
def index():
    news = get_news_from_google()
    return {'result': news}


def get_news_from_google():
    client = urlopen(news_url)
    page = client.read()
    client.close()
    souped = soup(page, "xml")
    news_list = souped.findAll("item")
    result = []
    for news in news_list:
        data = {}
        data['title'] = news.title.text
        data['date'] = news.pubDate.text
        result.append(data)
    return result
