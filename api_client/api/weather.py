from setup_logger import setup_logger
from time import sleep
import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load environment variables from .env file

logger = setup_logger(__name__)

def weather_emoji(description):
    d = description.lower()

    if "clear" in d:
        return "☀️"
    if "cloud" in d:
        return "☁️"
    if "rain" in d or "drizzle" in d:
        return "🌧️"
    if "storm" in d or "thunder" in d:
        return "⛈️"
    if "snow" in d:
        return "❄️"
    if "mist" in d or "fog" in d:
        return "🌫️"
    return "🌤️"

def build(id,data):
    if id == '1':
        emoji = weather_emoji(data["weather"][0].get("description"))
        print()
        print(f"{emoji}  Weather in {data.get("name")}, {data["sys"].get("country")}")
        print("———"*12)
        print(f"Temperature : {data["main"].get("temp")}°C (feels like {data["main"].get("feels_like")}°C)")
        print(f"Condition   : {data["weather"][0].get("description")}")
        print(f"Humidity    : {data["main"].get("humidity")}%")
        print(f"Wind        : {data["wind"].get("speed")} m/s")
        print(f"Visibility  : {data.get("visibility")//1000} km")
        print()

def display(data):
    print("Did you mean one of these??...")
    for index,value in enumerate(data, start=1):
        print(f"{[index]} Name : {value.get("name")} | State : {value.get("state")} | Country : {value.get("country")}")
    print()

def similar(data):
    f = False
    sim = input("OPT In : ")
    for index,value in enumerate(data, start=1):
        if sim in str(index):
            return value
            f = True
    if not f:
        print()
        try_again = input("Invalid OPT. Try Again [Y/n] : ").lower()
        if try_again == "y":
            similar(data)

def get_weather_openweather():
    api = os.environ["OPENWEATHER_API_KEY"]

    while True:
        city = input("Enter the city name: ")

        print()
        base = f"http://api.openweathermap.org/geo/1.0/direct"

        # Get city lon & lat
        params = {"q" : city, "limit": 5, "appid": api}
        response = requests.get(base,params = params)
        response.raise_for_status()
        info = response.json()

        if not info:
            logger.error("City not found... Please check the spelling and try again.")
            print()
            continue_search = input("Do you want to continue searching? (y/n): ")
            if continue_search.lower() != "y":
                break
            else:
                print()
                continue

        if len(info) == 1:
            for i in info:       
                lat = i["lat"]
                lon = i["lon"]

        if len(info) > 1:
            display(info)
            selected_info = similar(info)
            lat = selected_info["lat"]
            lon = selected_info["lon"]
            
        # Get city current weather
        current_base = "https://api.openweathermap.org/data/2.5/weather"
        current_params = {"lat": lat, "lon": lon, "units": "metric", "appid": api}
        current_response = requests.get(current_base, params=current_params)
        current_response.raise_for_status()
        current_data = current_response.json()

        logger.info("Fetching weather data...")
        print()
        build("1",current_data)

        continue_search = input("Do you want to continue searching? (y/n): ")
        if continue_search.lower() != "y":
            break
        print()



def get_weather_weatherapi():
    api = os.environ["WEATHERAPI_API_KEY"]
    city = input("Enter the city name: ")
    logger.info("Fetching weather data...")

    base = "http://api.weatherapi.com/v1/search.json"
    params = {"q" : city, "key" : api}
    response = requests.get(base,params=params)
    print(response.json())

get_weather_weatherapi()

