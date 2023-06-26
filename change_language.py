import speech_recognition as s_r
import pyttsx3
from termcolor import colored

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.setProperty("voice", voices[1].id)
    engine.say(audio)
    engine.runAndWait()

from translate import Translator
from googletrans import LANGUAGES
from termcolor import colored
def display_weather_report_in_different_language(weather_report):
    print(colored("Available languages:", "yellow"))
    for code, language in LANGUAGES.items():
        print(colored(f"{code}: {language}", "green"))
    
    target_language = input(colored("Enter the language code for translation: ", "yellow"))
    
    if target_language in LANGUAGES:
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(weather_report)
        print(colored(translated_text, "green"))
        speak(translated_text)
    else:
        print("Invalid language code.")
