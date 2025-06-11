import Pushover
from os import getenv
from dotenv import load_dotenv

def config() -> str:
    load_dotenv('../.env')
    api_key = getenv("api_key")
    user_key = getenv("user_key")
    return api_key, user_key

def main(api_key, user_key) -> None:
    thing = Pushover.Pushover(api_key, user_key)
    message = input("Message to send: ")
    thing.send_message(message)

if __name__ == "__main__":
    api_key, user_key = config()
    main(api_key, user_key)

