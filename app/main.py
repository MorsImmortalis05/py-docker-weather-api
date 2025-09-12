import os
import requests


def get_weather() -> dict:
    API_KEY=os.environ.get("API_KEY")
    FILTERING = "Paris"
    URL = f"http://api.weatherapi.com/v1/current.json?{API_KEY}&q={FILTERING}"
    response = requests.get(URL)
    data = response.json()
    return data


if __name__ == "__main__":
    get_weather()
