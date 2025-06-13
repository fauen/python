import requests as r

class WeatherInfo:
    def __init__(self):
        self.base_url = "https://wttr.in"

    def location_data(self, location):
        url = f"{self.base_url}/{location}"
        response = r.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to retrieve user data: {response.status_code}")

def main():
    #url = input("Input URL: ")
    location = input("Input location: ")
    
    api = WeatherInfo()
    weather_data = api.location_data(location)
    
    print(weather_data)
    

if __name__ == "__main__":
    main()
