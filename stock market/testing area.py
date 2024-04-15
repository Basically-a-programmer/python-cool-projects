import  requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

Twilo_sid = "AC3a4beed28f8eac1d4a8e1c89fe705840"
Twilo_token = "2ecf5133a74cdc4618734baa08fb8427"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key =  "XIYRI23W23425QK8"
news_api_key = "325b102b6995411da8ae3f81c9edcff9"

yesterday_Date = '2023-11-24'
day_before_Data = '2023-11-22'

news_param = {
    'q': COMPANY_NAME,
    'from':yesterday_Date,
    'sortBy':'popularity',
    'apiKey':news_api_key
}

stock_param = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK_NAME,
    'outputsize':'compact',
    'datatype':"json",
    "apikey": stock_api_key
}

stock_request = requests.get(STOCK_ENDPOINT,params=stock_param)
stock_request.raise_for_status()

stock_data = stock_request.json()
print(stock_data)
