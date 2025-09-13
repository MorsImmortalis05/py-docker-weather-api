import os
import requests


def validate(parameter):
    if parameter is None:
        raise ValueError(f"Requested data was not found in the response.")

def get_weather():
    API_KEY=os.environ.get("API_KEY")
    FILTERING = "Paris"
    URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={FILTERING}"
    response = requests.get(URL)
    data = response.json()
    current = data.get("current")
    validate(current)
    temperature = current.get("temp_c")
    validate(temperature)
    last_updated = current.get("last_updated")
    validate(last_updated)
    condition = current.get("condition")
    validate(condition)
    condition_text = condition.get("text")
    validate(condition_text)
    print(f"Paris/France {last_updated} "
          f"Weather: {temperature} Celsius, {condition_text}")


if __name__ == "__main__":
    get_weather()
