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
    url = f"https://atlas.microsoft.com/weather/severe/alerts/json?api-version=1.1&query={latitude},{longitude}&subscription-key={subscription_key}"
    response = requests.get(url)
    data = response.json()
    
    if data.get('results') == []:
        my_ans = "Perfect condition! No extreme conditions at present or in some few days"
        return my_ans
    else:
        alert = data['results'][0]['alertAreas'][0]
        alert_name = alert['name']
        alert_summary = alert['summary']
        alert_details = alert['alertDetails']

        # Extract the latest status
        latest_status = alert['latestStatus']['english']

        # Convert the details to string format
        output = f"\nAlert Name: {alert_name}\n\nSummary: {alert_summary}\nLatest Status: {latest_status}\n\nDetails:\n{alert_details}"
        print(colored(output, "blue"))
        speak(output)
        return output


def extreme_conditions():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    paraa = data.get("loc")
    my_paraa = paraa.split(",")
    
    latitude = (my_paraa[0])
    longitude = (my_paraa[1])
    
    # Canada latitude and longitude for extreme conditions
    # to check for canada comment out line 30, 31 and remove comment from below two lines. 
    # latitude = 48.057
    # longitude = -81.091
    subscription_key = os.environ.get("Azure_Api_Key")
    
    weather_data = get_weather_conditions(latitude, longitude, subscription_key)
    #print(weather_data)