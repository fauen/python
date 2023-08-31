import requests
import json

api_key = ""

city_name = input("Input city: ")
city_url = "http://api.openweathermap.org/geo/1.0/direct?q="
city_request = requests.get(f"{city_url}{city_name}&appid={api_key}")
city_response = json.loads(city_request.text)
lon = round(city_response[0]["lon"],2)
lat = round(city_response[0]["lat"],2)

weather_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&"
weather_request = requests.get(f"{weather_url}lat={lat}&lon={lon}&appid={api_key}")
print("Feels like:", round(weather_request.json()["main"]["feels_like"],1))
print(weather_request.json()["weather"][0]["description"].capitalize())