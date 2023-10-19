import requests as req
import json
import tkinter as tk
from tkinter import ttk

def fetch_data(key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"
    response=req.get(url)
    data = response.json()
    return data

def display_weather(data):
    for i in data["current"].values():

        print(i)
def display_current_data():
    selected_option = option_var.get()
    data = weather_data["current"]
    
    if selected_option == "Temperature (°C)":
        result_label.config(text=f"Temperature: {data['temp_c']} °C")
    elif selected_option == "Temperature (°F)":
        result_label.config(text=f"Temperature: {data['temp_f']} °F")
    # Add more options and data display here
root = tk.Tk()
root.title("Weather Data Viewer")

option_var = tk.StringVar(value="Temperature (°C)")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

options = [
    "Temperature (°C)",
    "Temperature (°F)",
]

option_label = ttk.Label(frame, text="Select Data:")
option_label.grid(row=0, column=0, padx=5, pady=5)

option_menu = ttk.Combobox(frame, textvariable=option_var, values=options)
option_menu.grid(row=0, column=1, padx=5, pady=5)

fetch_button = ttk.Button(frame, text="Fetch Data", command=display_current_data)
fetch_button.grid(row=0, column=2, padx=5, pady=5)

result_label = ttk.Label(frame, text="", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()



if __name__ == "__main__":
    key="0ee51b4c06dd49b3b80163216231910"
    city = input("Enter a city: ")
    weather_data = fetch_data(key, city)
    display_weather(weather_data)


