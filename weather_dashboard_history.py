import streamlit as st
import requests
import datetime

# Free WeatherStack API Key
API_KEY = "3dc8a24b2a5ef1fc69dc43df9cb6d264"
BASE_URL = "http://api.weatherstack.com"

# Streamlit App Title
st.title("🌤 Live & Historical Weather Dashboard")

# User Input for City
city = st.text_input("Enter City Name", "New Delhi")

# Fetch Current Weather Data
def get_current_weather(city):
    params = {"access_key": API_KEY, "query": city}
    response = requests.get(f"{BASE_URL}/current", params=params)
    return response.json()

# Fetch Historical Weather Data for Last 10 Days
def get_historical_weather(city):
    historical_data = {}
    today = datetime.date.today()

    for i in range(1, 11):  # Last 10 days
        date = today - datetime.timedelta(days=i)
        params = {"access_key": API_KEY, "query": city, "historical_date": date.strftime("%Y-%m-%d")}
        response = requests.get(f"{BASE_URL}/historical", params=params)
        data = response.json()

        if "historical" in data:
            historical_data[date.strftime("%Y-%m-%d")] = data["historical"][date.strftime("%Y-%m-%d")]

    return historical_data

# Display Weather Data on Button Click
if st.button("Get Weather"):
    current_data = get_current_weather(city)

    # Display Current Weather Data
    if "current" in current_data:
        weather = current_data["current"]
        
        st.subheader(f"🌍 Current Weather in {city}")
        st.write(f"**Temperature:** {weather['temperature']}°C")
        st.write(f"**Weather Condition:** {weather['weather_descriptions'][0]}")
        st.write(f"**Humidity:** {weather['humidity']}%")
        st.write(f"**Wind Speed:** {weather['wind_speed']} km/h")
    else:
        st.error("Error fetching current weather data. Please check the city name.")

    # Fetch and Display Historical Weather Data
    st.subheader(f"📅 Historical Weather (Last 10 Days) for {city}")
    historical_data = get_historical_weather(city)

    if historical_data:
        for date, data in historical_data.items():
            st.write(f"**📆 Date: {date}**")
            st.write(f"🌡 Temperature: {data['temperature']}°C")
            st.write(f"🌧 Weather: {data['weather_descriptions'][0]}")
            st.write(f"💧 Humidity: {data['humidity']}%")
            st.write(f"🌬 Wind Speed: {data['wind_speed']} km/h")
            st.write("---")  # Separator for readability
    else:
        st.error("Error fetching historical weather data.")
