import speech_recognition as sr
import pyttsx3
from utils.weather_api import fetch_weather
from utils.weather_parser import parse_weather_data
import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()


# API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")
API_KEY = "6478d4b6a334141f6703dcc77737ac34"
API_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_historical_weather(city, date):
    params = {
        "q": city,
        "appid": API_KEY,
        "date": date
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        raise Exception("Error fetching weather data")


def parse_weather_data(weather_data):
    temperature_kelvin = weather_data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]
    precipitation = weather_data.get("rain", {}).get("1h", 0.0)
    parsed_data = {
        "Temperature": f"{temperature_celsius} °C",
        "Humidity": f"{humidity}%",
        "Description": description,
        "Wind Speed": f"{wind_speed} m/s",
        "Precipitation": f"{precipitation} mm"
    }
    return parsed_data


def display_weather_data(weather_data):
    fig = plt.figure(figsize=(6, 4))
    colors = ['#FF7F50', '#00CED1', '#FFD700', '#32CD32', '#FF1493']
    fig.patch.set_facecolor('#F0F0F0')
    data = weather_data.copy()
    del data["Description"]
    temperature = float(data["Temperature"].split()[0])
    data["Temperature"] = f"{temperature:.2f} °C"
    plt.bar(data.keys(), data.values(), color=colors)
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.title('Weather Data')
    plt.tight_layout()
    plt.show()
