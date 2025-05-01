from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables before creating app
load_dotenv()

app = Flask(__name__)

# Configure Flask from environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Get API key from environment
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Development-specific settings
if os.getenv('FLASK_ENV') == 'development':
    app.debug = True

def get_weather_by_coordinates(api_key, lat, lon):
    try:
        # Get current weather
        current_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        current_response = requests.get(current_url)
        current_response.raise_for_status()
        current_weather = current_response.json()

        # Get 5-day forecast (3-hour intervals)
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        hourly_forecast = forecast_response.json()

        return {
            'current': current_weather,
            'hourly': hourly_forecast['list'][:12]  # Next 12 periods (3-hour intervals)
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/weather')
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if lat and lon:
        weather_data = get_weather_by_coordinates(WEATHER_API_KEY, lat, lon)
        if weather_data:
            return jsonify(weather_data)
        else:
            return {"error": "Error fetching weather data."}, 500
    return {"error": "No location provided."}, 400

if __name__ == '__main__':
    app.run()