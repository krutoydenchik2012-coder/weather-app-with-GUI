from urllib import response

import requests
import os

def get_weather(city: str) -> dict | None:
    api_key = os.getenv("API_KEY")
    
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric&lang=ru"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return None
   
    data = response.json()
    return {"city":        data["name"],
        "temp":        data["main"]["temp"],
        "feels_like":  data["main"]["feels_like"],
        "humidity":    data["main"]["humidity"],
        "description": data["weather"][0]["description"],
}

        