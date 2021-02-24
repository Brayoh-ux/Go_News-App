from config import newsapi

def get_news():
    news_api = newsapi
    top_headlines = news_api.get_top_headlines(sources="al-jazeera-english")

   

    