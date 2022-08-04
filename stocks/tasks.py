from django.conf import settings
from .serializers import NewsWriteSerializer
import datetime
from celery import shared_task
import requests
from core.celery import app
TICKERS = (
    "TSLA", "FB", "AMZN", "TWTR", "NFLX"
)
@app.task
def get_news_by_stock(stock: str):
    to = datetime.datetime.today().strftime("%Y-%m-%d")
    news = requests.get("""https://finnhub.io/api/v1/company-news?symbol={}&from={}&to={}&token={}""".format(stock, to, to, settings.FINHUB_AUTH_KEY))
    if news.status_code==200:
        serializer = NewsWriteSerializer(data=news.json(), many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return "FOUND"
    return "NOT FOUND"


@app.on_after_finalize.connect
def set_periodic_tasks(sender,**kwargs):
    for ticker in TICKERS:
        sender.add_periodic_task(10.0, get_news_by_stock.s(ticker))
    print("DONE")