import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")
API_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_historical_weather(city, date):
    params = {
        "q": city,
        "appid": API_KEY,
        "dt": date.timestamp() 
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
        "Temperature": (temperature_celsius, "°C"),
        "Humidity": (humidity, "%"),
        "Description": (description, ""),
        "Wind Speed": (wind_speed, "m/s"),
        "Precipitation": (precipitation, "mm")
    }
    return parsed_data

def display_weather_data(weather_data):
    dates = list(weather_data.keys())
    metrics = list(weather_data[dates[0]].keys())

    num_metrics = len(metrics)
    fig, axs = plt.subplots(num_metrics, 1, figsize=(10, 6), sharex=True)

    colors = plt.cm.get_cmap('tab10', num_metrics)  
    for i, metric in enumerate(metrics):
        values = [weather_data[date][metric][0] for date in dates]
        units = weather_data[dates[0]][metric][1]
        axs[i].plot(dates, values, marker='o', linestyle='-', color=colors(i), label=metric) 
        axs[i].set_ylabel(units)
        axs[i].legend()

    axs[-1].set_xlabel('Dates')
    fig.suptitle('Weather Parameter Variation')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def fetch_and_display_historical_weather(city, start_date, num_days):
    data = {}

    for i in range(num_days):
        date = start_date + timedelta(days=i)
        weather_data = fetch_historical_weather(city, date)
        parsed_data = parse_weather_data(weather_data)
        data[date.strftime('%Y-%m-%d')] = parsed_data

    display_weather_data(data)


