import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_API = "0U22EKBBAC64T6T2"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "58fca31d8dd54a4fad354b806b3e15e4"
TWILIO_SID = "AC20c477f61dfb1f878825db63e9804202"
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_NUMBER = "+16063572289"

def get_news():
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=os.environ.get("MY_NUMBER")
        )

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API
}

response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
percentage = (difference * 100) / float(yesterday_closing_price)

if percentage > 5:
    get_news()


