import requests as r
from configparser import ConfigParser
import os.path
import os

config = ConfigParser()

if not os.path.isfile('./config.ini'):
    token_input = input("Input your token: ")
    config['joplin'] = {
        "token": token_input
    }
    with open('./config.ini', 'w') as conf:
        config.write(conf)
    config.read('./config.ini')
else:
    config.read('./config.ini')

url = 'http://localhost:41184/notes?token='
token = config.get('joplin', 'token')
while True:
    title = input("Title: ")
    body = input("Body: ")
    data = {
        "title": title,
        "body": body
        }
    post = r.post(url=url + token, json=data)
    os.system('cls' if os.name == 'nt' else 'clear')
    if not post.status_code == 200:
        print(post.status_code)
        print(post.reason)
        quit()

# To-Do:
# Tag newly created notes
# Make sure it's moved to the correct folder/notebook