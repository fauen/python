import requests
import json

def main() -> None:
    url = 'https://zenquotes.io/api/today'
    response = requests.get(url=url)
    print(response.json()[0]['q'])
    print("- " + response.json()[0]['a'])

if __name__ == "__main__":
    main()
