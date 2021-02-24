from flask import Flask,render_template
from newsapi import NewsApiClient
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='e0bd6d205f124726aa45065db44bedda')
    top_headlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = top_headlines['articles']

#     desc = []
#     news = []
#     img = []
#     readmore = []
#     published = []

#     for i in range(len(articles)):
#         myarticles = articles[i]
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         published.append(myarticles['publishedAt'])
#         readmore.append(myarticles['url'])
#     mylist = zip(desc, news, img, readmore, published)

#     return render_template('index.html', context = mylist)


# @app.route('/bbc')
# def bbc():
#     newsapi = NewsApiClient(api_key='e0bd6d205f124726aa45065db44bedda')
#     top_headlines = newsapi.get_top_headlines(sources="bbc-news")

#     articles = top_headlines['articles']

#     desc = []
#     news = []
#     img = []
#     published = []
#     readmore = []

#     for i in range(len(articles)):
#         myarticles = articles[i]
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         published.append(myarticles['publishedAt'])
#         readmore.append(myarticles['url'])

#     mylist = zip(desc, news, img, published, readmore)

#     return render_template('bbc.html', context = mylist)


# if __name__=="__main__":
#     app.run(debug=True)