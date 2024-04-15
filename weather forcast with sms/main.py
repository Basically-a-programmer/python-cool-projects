import requests
import os

api_key = "f2493a82910e4ce012a0661f1d6bef0f"

weather_par = {
    'lat' : 11.916064,
    'lon':  79.812325,
    'appid': "f2493a82910e4ce012a0661f1d6bef0f",
    'cnt': 4
}

print(os.environ.get("we_app"))
request = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=weather_par)
request.raise_for_status()

data = request.json()
# print(data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True

if will_rain:
    print("Bring umbrella")