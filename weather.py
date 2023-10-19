import requests as req
import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO 
def fetch_data(key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"
    response = req.get(url)
    data = response.json()
    return data

def display_weather():
    city = city_in.get()
    key = "0ee51b4c06dd49b3b80163216231910"
    weather_data = fetch_data(key, city)
    selected_option = option_var.get()
    data = weather_data["current"]
    
    temp_c_label.config(text=f"Temperature: {data['temp_c']} °C")
    temp_f_label.config(text=f"Temperature: {data['temp_f']} °F")
    time_label.config(text=f"Time in {city} : {data['last_updated']}")
    condition_label.config(text=f"")
    if selected_option == "Temperature (°C)":
        temp_c_label.config(text=f"Temperature: {data['temp_c']} °C")
    elif selected_option == "Temperature (°F)":
        temp_f_label.config(text=f"Temperature: {data['temp_f']} °F")
    elif selected_option == "Time":
        time_label.config(text=f"Time in {city} : {data['last_updated']}")
    elif selected_option == "Condition":
        response=req.get("http:"+str(data["condition"]["icon"]))
        image_data = Image.open(BytesIO(response.content))
        image = ImageTk.PhotoImage(image_data)
        image_label.configure(image=image)
        image_label.image = image 
        time_label.config(text=f"Condition in {city} : {data['condition']['text']}")

    

root = tk.Tk()
root.title("Weather Data Viewer")
root.geometry("420x300")  # Increase the size

option_var = tk.StringVar(value="Temperature (°C)")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

options = [
    "Temperature (°C)",
    "Temperature (°F)",
    "Time",
    "Condition",
]

city_label = ttk.Label(frame, text="Enter City:")
city_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

city_in = ttk.Entry(frame, font=("Roboto", 12)) 
city_in.grid(row=0, column=1, padx=5, pady=5, sticky="w")

option_label = ttk.Label(frame, text="Select Data:")
option_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

option_menu = ttk.Combobox(frame, textvariable=option_var, values=options)
option_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

fetch_button = ttk.Button(frame, text="Fetch Data", command=display_weather)
fetch_button.grid(row=1, column=2, padx=5, pady=5, sticky="w")

temp_c_label = ttk.Label(frame, text="", font=("Roboto", 14))  
temp_c_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="w")
temp_f_label = ttk.Label(frame, text="", font=("Roboto", 14))  
temp_f_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="w")
time_label = ttk.Label(frame, text="", font=("Roboto", 14))  
time_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="w")
condition_label = ttk.Label(frame, text="", font=("Roboto", 14))  
condition_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="w")
image_label = ttk.Label(frame, text="", font=("Roboto", 14))  
image_label.grid(row=6, column=3, columnspan=3, padx=5, pady=5, sticky="w")


root.mainloop()