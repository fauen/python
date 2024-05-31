import requests as r
from dotenv import load_dotenv
from os import getenv

load_dotenv('../.env')

def get_weather(location="Stockholm"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={getenv('owm_key')}&units=metric"
    response = r.get(url).json()
    return response

if __name__ == "__main__":
    location = input("Input city: ")
    weather_data = get_weather(location)
    w_description = weather_data['weather'][0]['description'].capitalize()
    w_temp = weather_data['main']['temp']
    w_feels_like = weather_data['main']['feels_like']
    w_name = weather_data['name']
    print(f"{w_description}\n{w_temp}\n{w_feels_like}\n{w_name}")