import streamlit as st
import requests

# Free Weather API
API_KEY = "3dc8a24b2a5ef1fc69dc43df9cb6d264"
BASE_URL = "http://api.weatherstack.com/current"

# Streamlit App Title
st.title("🌤 Live Weather Dashboard")

# User Input for City
city = st.text_input("Enter City Name", "New Delhi")

# Fetch Weather Data
if st.button("Get Weather"):
    params = {"access_key": API_KEY, "query": city}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "current" in data:
        weather = data["current"]
        
        # Display Weather Data
        st.write(f"### 🌍 City: {city}")
        st.write(f"**Temperature:** {weather['temperature']}°C")
        st.write(f"**Weather Condition:** {weather['weather_descriptions'][0]}")
        st.write(f"**Humidity:** {weather['humidity']}%")
        st.write(f"**Wind Speed:** {weather['wind_speed']} km/h")
    else:
        st.error("Error fetching weather data. Please check the city name.")