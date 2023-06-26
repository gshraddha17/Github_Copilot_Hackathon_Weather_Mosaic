import requests
import json
import json
from urllib.request import urlopen
from utils.weather_api import fetch_weather
from utils.weather_parser import parse_weather_data
from termcolor import colored
import speech_recognition as s_r
import pyttsx3
from termcolor import colored
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.setProperty("voice", voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def daily_forecast(latitude, longitude,duration, subscription_key):
    url = f"https://atlas.microsoft.com/weather/forecast/hourly/json?api-version=1.1&query={latitude},{longitude}&duration={duration}&subscription-key={subscription_key}"
    
    response = requests.get(url)
    data = response.json()
    
    for i in range(0, 3):
        forecast = data['forecasts'][i]

        # Extract the desired details
        date = forecast['date'][:18].replace("T", " ")
        cloud_cover = forecast['cloudCover']
        icon_phrase = forecast['iconPhrase']
        temperature = forecast['temperature']['value']
        rain_probability = forecast['rainProbability']
        snow_probability = forecast['snowProbability']
        #uv_index_phrase = forecast['uvIndexPhrase']

        # Convert the details to string format
        output = f"Date: {date}\n\nCloud Cover: {cloud_cover}%\nWeather Type: {icon_phrase}\nTemperature: {temperature}°C\nRain Probability: {rain_probability}%\nSnow Probability: {snow_probability}%\n\n"
        print(colored(output, "blue"))
        speak(output)
    return output

def forecast_hourly():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    paraa = data.get("loc")
    my_paraa = paraa.split(",")
    
    latitude = (my_paraa[0])
    longitude = (my_paraa[1])
    subscription_key = os.environ.get("Azure_Api_Key")
    
    weather_data = daily_forecast(latitude, longitude,12, subscription_key)
    #print(weather_data)