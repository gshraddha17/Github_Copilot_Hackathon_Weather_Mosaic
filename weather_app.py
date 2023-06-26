import os
from dotenv import load_dotenv
load_dotenv()

from utils.weather_api import fetch_weather
from utils.weather_parser import parse_weather_data

def weather_report(city_name):
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

    if not api_key:
        return "Please provide your OpenWeatherMap API key."

    weather_data = fetch_weather(city_name, api_key)
    temperature, humidity, feels_like, temp_min, temp_max, pressure, visibility, wind_speed, latitude, longitude = parse_weather_data(weather_data)

    if temperature is not None and humidity is not None:
        report = f"Temperature: {temperature}K\n"
        report += f"Humidity: {humidity}%\n"
        report += f"Feels like: {feels_like}K\n"
        report += f"Minimum Temperature: {temp_min}K\n"
        report += f"Maximum Temperature: {temp_max}K\n"
        report += f"Pressure: {pressure}hPa\n"
        report += f"Visibility: {visibility}m\n"
        report += f"Wind Speed: {wind_speed}m/s\n"
        report += f"Latitude: {latitude}°\n"
        report += f"Longitude: {longitude}°"
        return report

