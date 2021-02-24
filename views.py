from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from config import newsapi

app = Flask(__name__)

bootstrap = Bootstrap(app)
@app.route('/')
def index():
    news_api = newsapi
    top_headlines = news_api.get_top_headlines(sources="al-jazeera-english")

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    readmore = []
    published = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        published.append(myarticles['publishedAt'])
        readmore.append(myarticles['url'])
    mylist = zip(desc, news, img, readmore, published)

    return render_template('index.html', context = mylist)

@app.route('/bbc')
def bbc():
    news_api = newsapi
    top_headlines = news_api.get_top_headlines(sources="bbc-news")

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    readmore = []
    published = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        published.append(myarticles['publishedAt'])
        readmore.append(myarticles['url'])
    mylist = zip(desc, news, img, readmore, published)

    return render_template('bbc.html', context = mylist)