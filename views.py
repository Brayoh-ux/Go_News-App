from flask import Flask,render_template, url_for
from flask_bootstrap import Bootstrap
from config import newsapi,source_url

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

@app.route('/source')
def source():
    new_api = newsapi
    sources_url = source_url.format(new_api)
    source = new_api.get_sources(category='general')

    sources = source['sources']

    myid = []
    name = []
    url = []
    desc = []

    for a in range(len(sources)):
        mysource = sources[a]
        myid.append(mysource['id'])
        name.append(mysource['name'])
        url.append(mysource['url'])
        desc.append(mysource['description'])

    mylist = zip(myid, name, url, desc)

    return render_template('source.html', context = mylist)