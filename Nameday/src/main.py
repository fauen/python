from datetime import date
import requests
import json

def main():
    today = date.today().strftime("%Y/%m/%d")
    url = f"https://sholiday.faboul.se/dagar/v2.1/{today}"
    response = requests.get(url)
    response = response.text
    data = json.loads(response)
    print(data["dagar"][0]["namnsdag"])

if __name__ == "__main__":
    main()
