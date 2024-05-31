from flask import Flask, render_template, request
from waitress import serve
from weather import get_weather

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_current_weather():
    city = request.args.get('city')
    weather_data = get_weather(city)

    return render_template(
        "weather.html",
        w_name = weather_data['name'],
        w_temp = weather_data['main']['temp'],
        w_feels_like = weather_data['main']['feels_like'],
        w_description = weather_data['weather'][0]['description'].capitalize()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    #serve(app, host="0.0.0.0", port=8000)