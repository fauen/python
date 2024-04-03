import requests as r
import json
from dotenv import load_dotenv
from os import getenv

def config():
    load_dotenv('../.env')
    key = getenv('key')
    if not key:
        key = input('Input key: ')
    return key

def main():
    package = input('Input package name: ')
    url = f'https://pypi.org/pypi/{package}/json'
    response = r.get(url=url)
    response = response.json()
    print(f"Name: {response['info']['name']}\nSummary: {response['info']['summary']}")

if __name__ == "__main__":
    # config()
    main()