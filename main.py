import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"The temperature in {city} is {temp}°C with {desc}.")
    elif response.status_code == 404:
        print(f"City '{city}' not found.")
    else:
        print(f"Error: {data.get('message', 'Unable to retrieve data')}")


while True:
    city = input("Enter a city name (or type 'exit' to quit ")
    if city.lower() == 'exit':
        break
    get_weather(city)
