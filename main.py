import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("API_KEY")
LAT=27.712021
LONG=85.312950
Account_ssid=os.getenv("ACCOUNT_SSID")
Auth_token=os.getenv("AUTH_TOKEN")

PARAMETERS={
    "lat":LAT,
    "lon":LONG,
    "cnt":4,
    "appid":api_key
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=PARAMETERS)
data=response.json()

will_rain=False
for hour_data in data["list"]:
    condition_codes=hour_data["weather"][0]["id"]
    if int(condition_codes)<600:
        will_rain=True
if will_rain:
    client=Client(Account_ssid,Auth_token)
    message=client.messages.create(
        body="Its going to rain.Bring an umbrella",
        from_= os.getenv("TWILIO_NUM"),
        to = os.getenv("PHONE_NUM")
    )
    print(message.status)

