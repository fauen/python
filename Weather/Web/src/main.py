import requests as r
from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/weather')
def get_weather():
    weather = r.get('https://wttr.in/?format=3')
    weather = weather.text
    return weather

if __name__ == "__main__":
    app.run()