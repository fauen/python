import requests as r
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='../www')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/weather')
def get_weather():
    weather = r.get('https://wttr.in/?format=3')
    weather = weather.text
    return weather

@app.route('/<name>', methods=['POST'])
def get_specific_weather(name):
    weather = r.get(f'https://wttr.in/{name}?format=3')
    weather = weather.text
    return weather

if __name__ == "__main__":
    app.run()