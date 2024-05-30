from dotenv import load_dotenv
from pprint import pprint as pp
from os import getenv
import requests as r

load_dotenv('../.env')

def get_current_weather(city="Stockholm"):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={getenv("API_KEY")}&q={city}&units=metric"
    data = r.get(url=url).json()
    return data

def main():
    data = get_current_weather()

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("Please enter a city name: ")
    if not bool(city.strip()):
        city= "Stockholm"
    data = get_current_weather(city)
    pp(data)