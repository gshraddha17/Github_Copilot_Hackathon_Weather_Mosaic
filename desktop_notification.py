import requests
import datetime 
import time 
from plyer import notification
from win10toast import ToastNotifier
import os
from dotenv import load_dotenv
load_dotenv()


def get_weather_data(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data
  
def main() -> None:
    # Retrieve the necessary environment variables
    api_key = os.environ["OPENWEATHERMAP_API_KEY"]
    location = os.environ["WeatherLocation"]    
    weather_data = get_weather_data(api_key, location)
    
    # Extract relevant information from the weather data
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    feels_like = weather_data['main']['feels_like']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    
    # Create the message to be sent
    mess = f"Weather update:\nTemperature: {temperature}K\nHumidity: {humidity}\nFeels Like: {feels_like}\nMinimum temperature: {temp_min}\nMaximum Temperature: {temp_max}%"
    #n = ToastNotifier()
    #n.show_toast("Weather App", message, duration = 30,icon_path ="weather.png") 
    notification.notify(title = "Weather : {}".format(datetime.date.today()), message = mess,  timeout  = 30  )  

#notification for everday
while(True):
    main()
    time.sleep(60*60*24)