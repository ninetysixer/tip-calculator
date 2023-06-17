import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = '21d3220882202f624a220c5975034230'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def get_weather_info(event=None):
    city = entry.get()
    if city:
        try:
            weather_data = get_weather(city)
            weather = weather_data['weather'][0]['main']
            temperature = weather_data['main']['temp']
            city = city.title()  # Capitalize the first letter of each word
            city_name_label['text'] = f'City: {city}'
            weather_label['text'] = f'Weather: {weather}'
            temperature_label['text'] = f'Temperature: {temperature}°C'
            entry.delete(0, tk.END)  # Clear the entry field
            city_name_label.pack()
            weather_label.pack()
            temperature_label.pack()
        except requests.exceptions.RequestException:
            messagebox.showerror('Error', 'An error occurred while fetching weather data.')
    else:
        messagebox.showwarning('Warning', 'Please enter a city name.')

# Create the GUI window
window = tk.Tk()
window.title('Weather Application by semihdursungul')
window.geometry('600x600')
window.configure(bg='orange')  # Set the background color of the main window to orange

# Create a frame to hold the widgets
frame = tk.Frame(window, bg='orange')  # Set the background color of the frame to yellow
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create and pack the widgets
label = tk.Label(frame, text='Enter a city name:', font=('Arial', 18))
label.pack()

entry = tk.Entry(frame, font=('Arial', 18))
entry.pack()
entry.focus_set()  # Automatically select the entry field
entry.bind('<Return>', get_weather_info)  # Bind the Enter key to the get_weather_info function

button = tk.Button(frame, text='Get Weather', command=get_weather_info, font=('Arial', 18))
button.pack()

city_name_label = tk.Label(frame, text='City:', font=('Arial', 18))
weather_label = tk.Label(frame, text='Weather:', font=('Arial', 18))
temperature_label = tk.Label(frame, text='Temperature:', font=('Arial', 18))

# Run the GUI loop
window.mainloop()
