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
    
def get_weather_conditions(latitude, longitude, subscription_key):
    url = f"https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.0&query={latitude},{longitude}&subscription-key={subscription_key}"
    
    response = requests.get(url)
    data = response.json()
    

    forecast = data['results'][0]

    # Extract the desired details
    date_time = forecast['dateTime'][:18].replace("T", " ")
    cloud_cover = forecast['cloudCover']
    icon_phrase = forecast['phrase']
    temperature = forecast['temperature']['value']
    rain_summary = forecast['precipitationSummary']['past12Hours']['value']

    output = f"Date/Time: {date_time}\n\nCloud Cover: {cloud_cover}%\nWeather Type: {icon_phrase}\nTemperature: {temperature}°C\nRain Summary (Past 12 Hours): {rain_summary}mm\n"

    print(colored(output, "blue"))
    speak(output)
    return output

def location_retrieval():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    paraa = data.get("loc")
    my_paraa = paraa.split(",")
    
    latitude = (my_paraa[0])
    longitude = (my_paraa[1])
    subscription_key = os.environ.get("Azure_Api_Key")
    
    weather_data = get_weather_conditions(latitude, longitude, subscription_key)
    
    


