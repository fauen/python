import requests
import json

api_key = ""

city_name = input("Input city: ")
city_url = "http://api.openweathermap.org/geo/1.0/direct?q="
city_request = requests.get(f"{city_url}{city_name}&appid={api_key}")
city_response = city_request.json()
print(type(city_response))

url = "https://api.openweathermap.org/data/2.5/weather?"

response = requests.get(f"{url}")