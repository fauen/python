import requests as r
from dotenv import load_dotenv
from os import getenv
from getpass import getpass as gp

def load_config():
    load_dotenv('../.env')
    key = getenv('key')
    if not key:
        key = gp("API key: ")
    return key

def autocomplete_search(key):
    search = input("What are you looking for? ")
    url = f"https://api.watchmode.com/v1/autocomplete-search/?apiKey={key}&search_value={search}&search_type=1"
    autocomplete = r.get(url=url)
    autocomplete = autocomplete.json()
    autocomplete = autocomplete["results"]
    for name in autocomplete:
        title = name["name"]
        name_id = name["id"]
        print(f"Title: {title}\nID: {name_id}\n")
    
def stream_search(key):
    source_id = input("Input ID: ")
    url = f"https://api.watchmode.com/v1/title/{source_id}/sources/?apiKey={key}"
    search_id = r.get(url=url)
    search_id = search_id.json()
    for item in search_id:
        name = item["name"]
        kind = item["type"]
        region = item["region"]
        if kind == "sub":
            print(f"Service: {name}\nType: {kind}\nRegion: {region}\n")
        
def main():
    key = load_config()
    autocomplete_search(key)
    stream_search(key)

if __name__ == "__main__":
    main()