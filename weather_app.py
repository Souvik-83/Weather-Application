import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    api_key = 'fd3186d8324de06e7d697f5309d7c26b'
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == '404':
            messagebox.showerror("Error", f"No weather data found for {city}.")
        else:
            weather = data['weather'][0]['main']
            temp_fahrenheit = data['main']['temp']
            temp_celsius = (temp_fahrenheit - 32) / 1.8
            messagebox.showinfo("Weather Info", f"Weather in {city}: {weather}\nTemperature: {temp_celsius:.1f}°C")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")

def fetch_weather():
    city_name = entry.get()
    get_weather(city_name)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create widgets
label = tk.Label(root, text="Enter city name:")
entry = tk.Entry(root)
button = tk.Button(root, text="Get Weather", command=fetch_weather)

# Pack widgets
label.pack()
entry.pack()
button.pack()

# Start the GUI event loop
root.mainloop()
