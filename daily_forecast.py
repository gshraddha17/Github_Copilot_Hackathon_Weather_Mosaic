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
    url = f"https://atlas.microsoft.com/weather/forecast/daily/json?api-version=1.1&query={latitude},{longitude}&duration={duration}&subscription-key={subscription_key}"
    
    response = requests.get(url)
    data = response.json()
    PrettyJson = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
    #print(PrettyJson)
    for i in range(0, duration):
        date = data['forecasts'][i]['date'][:10]
        #print(date)
        day = data['forecasts'][i]['day']
        #print(day)
        night = data['forecasts'][i]['night']
        hoursOfSun = data['forecasts'][i]['hoursOfSun']
        output = f"Date: {date}\n\nDay:\n- Hours of Rain: {day['hoursOfRain']}\n- Hours of Sun: {hoursOfSun}\n- Hours of Snow: {day['hoursOfSnow']}\n- Rain Probability: {day['precipitationProbability']}%\n- Short Phrase: {day['shortPhrase']}\n\nNight:\n- Hours of Rain: {night['hoursOfRain']}\n- Hours of Sun: {hoursOfSun}\n- Hours of Snow: {night['hoursOfSnow']}\n- Rain Probability: {night['precipitationProbability']}%\n- Short Phrase: {night['shortPhrase']}\n\n"
        print(colored(output, "blue"))
        speak(output)
    return output


def forecast_daily():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    

    paraa = data.get("loc")
    my_paraa = paraa.split(",")
    
    latitude = (my_paraa[0])
    longitude = (my_paraa[1])
    subscription_key = os.environ.get("Azure_Api_Key")
    duration = int(input(colored("How many days data you want, options = [1, 5, 10, 15, 25, 45]? = ", "green")))
    speak("How many days data you want")
    weather_data = daily_forecast(latitude, longitude, duration, subscription_key)
    #print(weather_data)
    


