{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4e580077-aef9-4f0f-ade6-3da15d2b831a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in ./anaconda3/lib/python3.11/site-packages (2.32.3)\n",
      "Requirement already satisfied: pandas in ./anaconda3/lib/python3.11/site-packages (2.2.3)\n",
      "Requirement already satisfied: streamlit in ./anaconda3/lib/python3.11/site-packages (1.42.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in ./anaconda3/lib/python3.11/site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in ./anaconda3/lib/python3.11/site-packages (from requests) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in ./anaconda3/lib/python3.11/site-packages (from requests) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.11/site-packages (from requests) (2025.1.31)\n",
      "Requirement already satisfied: numpy>=1.23.2 in ./anaconda3/lib/python3.11/site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in ./anaconda3/lib/python3.11/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in ./anaconda3/lib/python3.11/site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in ./anaconda3/lib/python3.11/site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: altair<6,>=4.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (5.5.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (13.9.4)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (3.1.44)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: jinja2 in ./anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in ./anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in ./anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (1.28.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in ./anaconda3/lib/python3.11/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: six>=1.5 in ./anaconda3/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in ./anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in ./anaconda3/lib/python3.11/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in ./anaconda3/lib/python3.11/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=22.2.0 in ./anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.3.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in ./anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in ./anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
      "Requirement already satisfied: mdurl~=0.1 in ./anaconda3/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests pandas streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b795fff9-053c-4cb8-bad5-f2f98bebbbb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-26 00:06:42.944 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.064 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/anupsharma/anaconda3/lib/python3.11/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-02-26 00:06:43.065 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.065 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.065 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.065 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.066 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.066 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.066 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.066 Session state does not function when running a script without `streamlit run`\n",
      "2025-02-26 00:06:43.066 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.067 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.067 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.067 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.067 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.067 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.068 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.068 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-26 00:06:43.068 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import streamlit as st\n",
    "\n",
    "# Free Weather API Key (Replace with your own)\n",
    "API_KEY = \"2d531fc6c63d47138c5183312252502\"  # Get from https://www.weatherapi.com/\n",
    "\n",
    "# Function to fetch weather data\n",
    "def get_weather(city):\n",
    "    url = f\"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no\"\n",
    "    response = requests.get(url)\n",
    "\n",
    "    if response.status_code == 200:\n",
    "        data = response.json()\n",
    "        return {\n",
    "            \"City\": data[\"location\"][\"name\"],\n",
    "            \"Country\": data[\"location\"][\"country\"],\n",
    "            \"Temperature (°C)\": data[\"current\"][\"temp_c\"],\n",
    "            \"Condition\": data[\"current\"][\"condition\"][\"text\"],\n",
    "            \"Humidity (%)\": data[\"current\"][\"humidity\"],\n",
    "            \"Wind Speed (km/h)\": data[\"current\"][\"wind_kph\"],\n",
    "            \"Last Updated\": data[\"current\"][\"last_updated\"],\n",
    "        }\n",
    "    else:\n",
    "        return None\n",
    "\n",
    "# Streamlit Dashboard UI\n",
    "st.title(\"🌤 Live Weather Dashboard\")\n",
    "st.sidebar.header(\"Enter City Name\")\n",
    "city = st.sidebar.text_input(\"City\", \"New Delhi\")\n",
    "\n",
    "if st.sidebar.button(\"Get Weather\"):\n",
    "    weather_data = get_weather(city)\n",
    "\n",
    "    if weather_data:\n",
    "        df = pd.DataFrame([weather_data])\n",
    "        st.write(\"### Current Weather Data:\")\n",
    "        st.dataframe(df)\n",
    "    else:\n",
    "        st.error(\"Failed to fetch weather data. Please check the city name or API key.\")\n",
    "\n",
    "st.sidebar.info(\"Data provided by WeatherAPI.com\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}