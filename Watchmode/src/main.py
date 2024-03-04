import requests as r
from getpass import getpass as gp
import json

def autocomplete_search():
    key = gp("API key: ")
    search = input("What are you looking for? ")
    url = f"https://api.watchmode.com/v1/autocomplete-search/?apiKey={key}&search_value={search}&search_type=1"
    response = r.get(url=url)
    data = (json.loads(response.text))
    print(json.dumps(data, indent=2))

def main():
    autocomplete_search()

if __name__ == "__main__":
    main()