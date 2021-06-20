import requests
from twilio.rest import Client

OWM_ENDPOINT = "owm_endpoint"  # Enter the OpenWeatherMap API endpoint
API_KEY = "api_key"  # Enter your your OpenWeatherMap API key
ACCOUNT_SID = "account_sid"  # Enter your your OpenWeatherMap account SID
AUTH_TOKEN = "auth_token"  # Enter your your OpenWeatherMap authorization token

MY_LAT = 0  # Enter your latitude
MY_LON = 0  # Enter your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an ☔.",
                from_="1234567890",  # Enter your outgoing phone number
                to="+1234567890", )  # Enter your incoming phone number
    print(message.status)
