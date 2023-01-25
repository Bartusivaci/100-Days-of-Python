import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

MY_LAT = 39.946411
MY_LON = 32.669102

account_sid = "AC20c477f61dfb1f878825db63e9804202"
auth_token = os.environ.get("AUTH_TOKEN")
twilio_number = "+16063572289"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # The weathers with codes lesser than 700 require an umbrella
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="You should take your umbrella with you today!",
                                     from_=twilio_number,
                                     to=os.environ.get("MY_NUMBER"))

    print(message.status)

