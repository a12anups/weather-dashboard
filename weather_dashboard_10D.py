import streamlit as st
import requests
import datetime

# Open-Meteo API Endpoint
OPEN_METEO_URL = "https://archive-api.open-meteo.com/v1/archive"

# Function to Get Latitude & Longitude from City Name
def get_city_coordinates(city):
    geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(geo_url).json()
    if response:
        return float(response[0]["lat"]), float(response[0]["lon"])
    return None, None

# Function to Fetch Historical Weather Data
def get_historical_weather(latitude, longitude):
    historical_data = {}
    today = datetime.date.today()

    for i in range(1, 11):  # Fetch last 10 days data
        date = today - datetime.timedelta(days=i)
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": date.strftime("%Y-%m-%d"),
            "end_date": date.strftime("%Y-%m-%d"),
            "hourly": "temperature_2m,humidity_2m,windspeed_10m",
        }
        response = requests.get(OPEN_METEO_URL, params=params)
        data = response.json()

        if "hourly" in data:
            historical_data[date.strftime("%Y-%m-%d")] = {
                "temperature": data["hourly"]["temperature_2m"][0],  # First hour's data
                "humidity": data["hourly"]["humidity_2m"][0],
                "wind_speed": data["hourly"]["windspeed_10m"][0],
            }
    return historical_data

# Streamlit App
st.title("🌦 Last 10 Days Historical Weather Dashboard")

# User Input for City
city = st.text_input("Enter City Name", "New Delhi")

# Display Weather Data on Button Click
if st.button("Get Weather"):
    latitude, longitude = get_city_coordinates(city)

    if latitude and longitude:
        historical_data = get_historical_weather(latitude, longitude)

        if historical_data:
            st.subheader(f"📅 Historical Weather (Last 10 Days) for {city}")

            for date, data in historical_data.items():
                st.write(f"**📆 Date: {date}**")
                st.write(f"🌡 Temperature: {data['temperature']}°C")
                st.write(f"💧 Humidity: {data['humidity']}%")
                st.write(f"🌬 Wind Speed: {data['wind_speed']} km/h")
                st.write("---")  # Separator for readability
        else:
            st.error("Error fetching historical weather data.")
    else:
        st.error("Could not retrieve city coordinates. Please check the city name.")
