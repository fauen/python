import requests as r
from dotenv import load_dotenv
from os import getenv

def config() -> str:
    load_dotenv("../.env")
    api_key = getenv('API_KEY')
    user_key = getenv('USER_KEY')
    return api_key, user_key

def main(api_key: str, user_key:str) -> None:
    url = "https://api.pushover.net/1/messages.json"   
    message = input("Input message: ")
    data = {
            "token": api_key,
            "user": user_key,
            "message": message
            }
    response = r.post(url = url, data = data)
    if response.status_code != 200:
        print(response)

if __name__ == "__main__":
    api_key, user_key = config()
    main(api_key, user_key)
