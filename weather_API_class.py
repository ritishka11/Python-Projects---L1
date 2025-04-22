# Import required libraries
import urllib.request      # To make HTTP requests to URLs (like APIs)
import json                # To parse JSON data
from urllib.error import HTTPError  # To handle specific HTTP errors

# Define a class to organize the weather functionality
class Weather:
    # Constructor: initializes with city name, API key, and base URL
    def __init__(self, city_name, API_key, base_URL):
        self.city_name = city_name
        self.API_key = API_key
        self.base_URL = base_URL
        # Creates the complete URL for the API request using the parameters
        self.complete_URL = f"{self.base_URL}?q={self.city_name}&appid={self.API_key}&units=metric"

    # This method fetches the weather data from the API
    def fetch_weather(self):
        try:
            # Sends the request and opens the response using 'with' to ensure it closes properly
            with urllib.request.urlopen(self.complete_URL) as response:
                data = response.read()  # Reads the response data (JSON string)
                weather_info = json.loads(data)  # Converts JSON string to a Python dictionary

            # Checks if city was not found (API returns cod "404")
            if weather_info["cod"] == "404":
                print("City not found")
                return None  # Returns nothing so display won't be shown
            else:
                return weather_info  # Return the weather data

        # If the request fails (like no internet, wrong URL, etc.)
        except HTTPError as err:
            print("Something went wrong with the request:", err.code)
            print("Error message:", err.reason)
            return None

    # This method displays the weather details
    def display_weather(self, weather_info):
        if weather_info:
            # Extract specific weather details
            main_data = weather_info["main"]
            weather_data = weather_info["weather"][0]

            temp = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_description = weather_data["description"]

            # Display the extracted info
            print(f"\nWeather in {self.city_name}:")
            print(f"Temperature: {temp}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_description}")
        else:
            print("No weather info available.")


# ------------ Main program starts here ------------ #

# Step 1: Ask user to enter a city name
city_name = input("Enter the city name: ")

# Step 2: Set your API key and the base URL for OpenWeatherMap
api_key = "9c44ec71147665bde2bc56dc5413e0c7"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Step 3: Create an instance of the Weather class
weather = Weather(city_name, api_key, base_url)

# Step 4: Call method to fetch data from API
weather_info = weather.fetch_weather()

# Step 5: Call method to display weather (only if data was fetched)
weather.display_weather(weather_info)
