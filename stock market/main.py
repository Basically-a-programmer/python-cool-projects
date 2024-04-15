import  requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

Twilo_sid = "AC3a4beed28f8eac1d4a8e1c89fe705840"
Twilo_token = "2ecf5133a74cdc4618734baa08fb8427"
twilo_virtual = "+14847026182"
user_number = "+919154630718"
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
yesterday_close = round(float(stock_data['Time Series (Daily)']['2023-11-24']['4. close']),2)

day_before_yesterday_Close = round(float(stock_data['Time Series (Daily)'][day_before_Data]['4. close']),2)

dif = (yesterday_close)-(day_before_yesterday_Close)
dif = round(abs(dif),2)

per = ((dif)/day_before_yesterday_Close)*1000
print(per)

if per>5:
    news_request = requests.get(NEWS_ENDPOINT, params=news_param)
    news_request.raise_for_status()

    news_data = news_request.json()
    articles = news_data['articles']
    article_Slice = slice(0, 2, 1)
    first_3_article = articles[article_Slice]
    client = Client(Twilo_sid, Twilo_token)
    for text_msg in first_3_article:
        print("hi")
        message = client.messages.create(

            body=text_msg,
            from_= twilo_virtual,
            to= user_number
        )
