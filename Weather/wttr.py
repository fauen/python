import requests as r

def GetWeather(city):
    url = f"https://wttr.in/{city}?m"
    get_weather = r.get(url)
    return get_weather.text

input_location = input("City: ")
print(GetWeather(input_location))