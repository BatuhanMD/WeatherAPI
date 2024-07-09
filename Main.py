import requests
import tkinter as tk
from tkinter import messagebox

weatherWindow = tk.Tk()
weatherWindow.minsize(width=300, height=200)
weatherWindow.title("Weather App")

city_label = tk.Label(weatherWindow, text="Select City:", font=("Arial", 12, "bold"))
city_label.pack(pady=10)

coordinates = {
    "Berlin": "52.520551,13.461804",
    "Paris": "48.856613,2.352222",
    "London": "51.507351,-0.127758",
    "New York": "40.712776,-74.005974",
    "Tokyo": "35.689487,139.691711",
    "Sydney": "-33.868820,151.209290",
    "Istanbul": "41.008240,28.978359",
    "Moscow": "55.755825,37.617298",
    "Beijing": "39.904202,116.407394",
    "Delhi": "28.613939,77.209023"
}

city_var = tk.StringVar(weatherWindow)
city_var.set(list(coordinates.keys())[0]) 

city_menu = tk.OptionMenu(weatherWindow, city_var, *coordinates.keys())
city_menu.pack(pady=10)

get_button = tk.Button(weatherWindow, text="Get Weather")
get_button.pack()

weather_label = tk.Label(weatherWindow, text="")
weather_label.pack()

def fetch_weather():
    city = city_var.get()
    user = "USERNAME"  # Meteomatics username
    password = "PASSWORD"  # Meteomatics password

    if city in coordinates:
        coord = coordinates[city]
        url = f"https://{user}:{password}@api.meteomatics.com/2024-07-09T00:00:00Z/t_2m:C/{coord}/json"
        
        try:
            response = requests.get(url)
            data = response.json()
            print(data)  
            temperature = data["data"][0]["coordinates"][0]["dates"][0]["value"]
            weather_label.config(text=f"Temperature: {temperature}°C")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to get weather data: {e}")
    else:
        messagebox.showerror("Error", "City not found in coordinates list")

get_button.config(command=fetch_weather)

weatherWindow.mainloop()