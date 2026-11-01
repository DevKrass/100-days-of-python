import os

import requests
import requests_cache
from dotenv import load_dotenv
from twilio.rest import Client

requests_cache.install_cache("stock_news_cache", expire_after=3600)  # Cache for 1 hour
requests_cache.install_cache("stock_data_cache", expire_after=3600)  # Cache for 1 hour

load_dotenv()  # Load environment variables from .env file

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Get API keys and Twilio credentials from environment variables
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_PHONE_NUMBER = os.getenv("FROM_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")
client = Client(ACCOUNT_SID, AUTH_TOKEN)

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=alpha_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

percentage_change = (
    (yesterday_closing_price - day_before_yesterday_closing_price)
    / day_before_yesterday_closing_price
) * 100

if abs(percentage_change) >= 5:
    direction = "🔺" if percentage_change > 0 else "🔻"

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    # Get the first 3 news pieces for the COMPANY_NAME
    news_articles = news_response.json()["articles"][:3]

    formatted_articles = [
        f"{STOCK}: {direction}{abs(percentage_change):.0f}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
        for article in news_articles
    ]

    # Send a seperate message with the percentage change and each article's title and description to your phone number

    # Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file with the SEC.

    or

    TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file with the SEC.
    """

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER,
        )
