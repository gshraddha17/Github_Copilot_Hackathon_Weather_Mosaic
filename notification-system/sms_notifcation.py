import os
import json
import datetime
import requests
from azure.cosmosdb.table.tableservice import TableService
from azure.functions import TimerRequest
from twilio.rest import Client

def get_weather_data(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def send_sms(account_sid, auth_token, twilio_number, recipient_number, message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=recipient_number
    )

def main(timer: TimerRequest) -> None:
    # Retrieve the necessary environment variables
    api_key = os.environ["OPENWEATHERMAP_API_KEY"]
    location = os.environ["WeatherLocation"]
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    twilio_number = os.environ["TwilioPhoneNumber"]
    recipient_number = os.environ["RecipientPhoneNumber"]
    
    # Get the current weather data
    weather_data = get_weather_data(api_key, location)
    
    # Extract relevant information from the weather data
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    
    # Create the message to be sent
    message = f"Weather update:\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    
    # Send the SMS notification
    send_sms(account_sid, auth_token, twilio_number, recipient_number, message)
