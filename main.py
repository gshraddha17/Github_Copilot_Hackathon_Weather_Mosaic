import time
import os
import random
import speech_recognition as s_r
import pyttsx3
from termcolor import colored
from weather_app import weather_report
from telegram_bot import use_telegram
from change_language import display_weather_report_in_different_language
from gps import location_retrieval
from historical_data import display_weather_data, fetch_historical_weather, parse_weather_data
import datetime
from visualization import fetch_and_display_historical_weather
from daily_forecast import forecast_daily
from hourly_forecast import forecast_hourly
from extreme_conditions_alert import extreme_conditions

def speak(audio):
    engine.setProperty("voice", voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def speech_input():
    r = s_r.Recognizer()
    with s_r.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=2.5)

    try:
        print("Recognizing! ", end="")
        move = r.recognize_google(audio, language="en-in")
        print(move)

    except Exception as e:
        speak("Say it again, please!")
        return "None"
    return move

def view_dashboard():
    print(colored("\t\t\t\t\t\t\t\t\t\tDashboard", "green"))
    for i in range(1, 6):
        print()
    commands = [
        ("Weather {city_name}", "View weather details of any city"),
        ("Change Language", "To get weather details in some other language"),
        ("Enable GPS", "Get weather report through GPS functionality"),
        ("Notifications", "Enable weather notifications on your phone"),
        ("Historical Data", "View historical weather data of any place"),
        ("Visualization", "View weather details of any city through graphs and visuals"),
        ("Save Data", "Save weather data for future use"),
        ("Telegram", "Access weather data using Telegram on any device"),
        ("Daily Forecast", "To see daily weather forecast"),
        ("Hourly Forecast", "To see hourly weather forecast"),
        ("Extreme Condition", "To know if the weather at your place is perfect or can there be some extreme conditions")
    ]

    instruction = "Type the command followed by any required parameters:\n"

    print(colored(instruction, "yellow"))
    time.sleep(0.5)
    speak(instruction)

    for command, description in commands:
        print(colored(f"{command}: {description}", "yellow"))
        time.sleep(0.5)
        speak(f"{command}: {description}")
    print()
    print()
    print()
    print()

def display_weather(city_name):
    print(colored("Weather Details of " + city_name + ":", "green"))
    speak("Weather Details of " + city_name)
    print()
    print()
    print(colored(weather_report(city_name), "yellow"))
    speak(weather_report(city_name))
    os.system("cls")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

if __name__ == "__main__":
    # for i in range(1, 15):
    #     print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print(colored("\t\t\t\t\t\t\t\tWeather Mosaic", "green"))
    speak("Hello, I am Weather Mosaic")
    speak("I will help you in getting a lot of details about the weather at any location")
    speak("At any point, you may enter 'help' to go to the dashboard section to see all the functionalities Weather Mosaic offers")
    print()
    print()
    print()
    print(colored("\t\t\t\t\t\tAt any point, you may type 'help' to view the dashboard", "blue"))
    for i in range(1, 15):
        print()

    input("Press Enter to continue...")
    clear_screen()
    while True:
        print(">", end="")
        s = input()
        clear_screen()
        if "help" in s.lower():
            view_dashboard()

        elif "weather" in s.lower():
            display_weather(s.split()[1])

        elif "language" in s.lower():
            city_name = input(colored("Enter city name: ", "yellow"))
            display_weather_report_in_different_language(weather_report(city_name))

        elif "gps" in s.lower():
            location_retrieval()

        elif "historical" in s.lower():
            speak("Enter the city name")
            city = input(colored("Enter the city name: ", "green"))
            speak("Enter date")
            date = input(colored("Enter date (YYYY-MM-DD): ", "green"))

            weather_data = fetch_historical_weather(city, date)
            parsed_data = parse_weather_data(weather_data)
            display_weather_data(parsed_data)
            
        elif "visualization" in s.lower():
            from datetime import datetime

            speak("Enter city name")
            city = input(colored("Enter city name: ", "green"))
            speak("Enter start date")
            start_date_str = input(colored("Enter start date(YYYY-MM-DD): ", "green"))
            start_date_parts = start_date_str.split("-")
            start_date = datetime(int(start_date_parts[0]), int(start_date_parts[1]), int(start_date_parts[2]))
            num_days = input(colored("Enter number of days: ", "green"))
            num_days = int(num_days)
            fetch_and_display_historical_weather(city, start_date, num_days)


        elif "notifications" in s.lower():
            # notification()
            i = 1

        elif "save" in s.lower():
            speak("Enter the city name and date; a graph will open with all details; click on the save button to save the data")
            speak("Enter the city name")
            city = input(colored("Enter the city name: ", "green"))
            speak("Enter date")
            date = input(colored("Enter date (YYYY-MM-DD): ", "green"))

            weather_data = fetch_historical_weather(city, date)
            parsed_data = parse_weather_data(weather_data)
            display_weather_data(parsed_data)

        elif "telegram" in s.lower():
            speak("Just type /weather city name on Telegram to access data")
            use_telegram()

        elif "daily" in s.lower():
            forecast_daily()
            
        elif "hourly" in s.lower():
            forecast_hourly()
            
        elif "extreme" in s.lower():
            extreme_conditions()
            