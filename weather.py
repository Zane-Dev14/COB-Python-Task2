import requests as req
import json
def fetch_data(key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"
    response=req.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    key="0ee51b4c06dd49b3b80163216231910"
    city = input("Enter a city: ")
    weather_data = fetch_data(key, city)
    display_weather(weather_data)


