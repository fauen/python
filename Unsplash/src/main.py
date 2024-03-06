import requests as r
import json
from getpass import getpass as gp

def Bearer():
    client_id = gp("Input id: ")
    client_secret = gp("Input secret: ")
    return client_id, client_secret

def Unsplash():
    key = gp("Input key: ")
    photo = input("What are you searchin for? ")
    url = f"https://api.unsplash.com/search/photos/query={photo}"
    response = r.get()

def main():
    pass

if __name__ == "__main__":
    main()