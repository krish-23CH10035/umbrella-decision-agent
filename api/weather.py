# Import necessary libraries
from flask import Flask, request, jsonify
import os
import requests

# Create the Flask app
app = Flask(__name__)

# This is the function that runs when our JavaScript calls /api/weather
@app.route('/api/weather', methods=['GET'])
def get_weather_advice():
    # Get the city name that the JavaScript sent
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # Securely get the API key that we will set up on the server later
    api_key = os.environ.get("62673c604484aafa925832f7110dd56c")
    if not api_key:
        return jsonify({"error": "Weather API key not configured"}), 500

    # Build the URL to call the OpenWeatherMap service
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Call the service and get the live weather data
    response = requests.get(url)
    
    # Handle cases where the city is not found
    if response.status_code != 200:
        return jsonify({"error": f"Could not find weather for '{city}'"}), 404

    # Extract the main weather condition from the data
    weather_data = response.json()
    main_weather = weather_data['weather'][0]['main']

    # --- THIS IS THE AGENT'S "REASONING" ---
    # A simple list of weather conditions that require an umbrella
    rain_conditions = ["Rain", "Drizzle", "Thunderstorm", "Squall"]
    
    if main_weather in rain_conditions:
        # If the weather matches, create a "Yes" suggestion
        suggestion = f"Yes, take an umbrella! The forecast shows: {main_weather}."
        bring_umbrella = True
        icon = "☔️"
    else:
        # If it doesn't match, create a "No" suggestion
        suggestion = f"No, you don't need an umbrella. The forecast is: {main_weather}."
        bring_umbrella = False
        icon = "☀️"

    # Send the final decision back to the JavaScript
    return jsonify({
        "suggestion": suggestion,
        "bringUmbrella": bring_umbrella,
        "icon": icon
    })