import requests
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        # API Setup (Replace with your actual API key from OpenWeatherMap)
        self.API_KEY = "556e428931c42d2c4ff1ca2951439b6f"
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        
        # UI Setup
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')
        
        self.create_ui()
    
    def create_ui(self):
        # City Entry
        tk.Label(self.root, text="Enter City Name", bg='#f0f0f0', font=('Arial', 12)).pack(pady=(20, 5))
        self.city_entry = tk.Entry(self.root, font=('Arial', 14), width=25)
        self.city_entry.pack(pady=10)
        
        # Search Button
        search_btn = tk.Button(self.root, text="Get Weather", command=self.get_weather, 
                               bg='#4CAF50', fg='white', font=('Arial', 12))
        search_btn.pack(pady=10)
        
        # Weather Display Frames
        self.weather_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.weather_frame.pack(pady=20)
    
    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
        
        try:
            # Fetch Weather Data
            params = {
                'q': city,
                'appid': self.API_KEY,
                'units': 'metric'  # Use metric for Celsius
            }
            response = requests.get(self.BASE_URL, params=params)
            weather_data = response.json()
            
            # Clear previous results
            for widget in self.weather_frame.winfo_children():
                widget.destroy()
            
            # Display Weather Information
            self.display_weather(weather_data)
        
        except requests.RequestException:
            messagebox.showerror("Network Error", "Unable to fetch weather data")
        except KeyError:
            messagebox.showerror("Error", "City not found or invalid API response")
    
    def display_weather(self, data):
        # City Name
        tk.Label(self.weather_frame, text=f"{data['name']}, {data['sys']['country']}", 
                 font=('Arial', 16, 'bold'), bg='#f0f0f0').pack()
        
        # Temperature
        temp = data['main']['temp']
        tk.Label(self.weather_frame, 
                 text=f"Temperature: {temp}°C", 
                 font=('Arial', 14), bg='#f0f0f0').pack()
        
        # Weather Description
        description = data['weather'][0]['description'].capitalize()
        tk.Label(self.weather_frame, 
                 text=f"Conditions: {description}", 
                 font=('Arial', 12), bg='#f0f0f0').pack()
        
        # Additional Details
        details = [
            f"Feels Like: {data['main']['feels_like']}°C",
            f"Humidity: {data['main']['humidity']}%",
            f"Wind Speed: {data['wind']['speed']} m/s"
        ]
        
        for detail in details:
            tk.Label(self.weather_frame, text=detail, 
                     font=('Arial', 12), bg='#f0f0f0').pack()
        
        # Timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tk.Label(self.weather_frame, text=f"Last Updated: {current_time}", 
                 font=('Arial', 10, 'italic'), bg='#f0f0f0').pack(pady=(10,0))

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()