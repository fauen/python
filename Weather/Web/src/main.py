import requests as r
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Amazing page</h1><a href="/weather">weather</a>'

@app.route('/weather')
def get_weather():
    weather = r.get('https://wttr.in/?format=3')
    weather = weather.text
    return weather

@app.route('/<name>')
def get_specific_weather(name):
    weather = r.get(f'https://wttr.in/{name}?format=3')
    weather = weather.text
    return weather

if __name__ == "__main__":
    app.run()