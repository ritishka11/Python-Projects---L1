#is the library for handling URLs in Python.
#urllib.request is a submodule that specifically deals with opening and reading URLs.
import urllib.request
import json
city_name = input("Enter the city name: ")

api_key = "9c44ec71147665bde2bc56dc5413e0c7"
base_url = "https://api.openweathermap.org/data/2.5/weather"
complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

#By using urllib.request.urlopen(), we can fetch data from an API by sending an HTTP GET request.
#with: This is a context manager in Python. It’s used to ensure that resources are properly managed. In this case, with ensures that the connection to the URL is properly closed after the response is fetched, even if an error occurs.
#The response object holds the raw data returned by the OpenWeatherMap API. In your case, this would be a JSON object containing the weather information. You can think of it like a box that contains the data from the server.

with urllib.request.urlopen(complete_url) as response:
    data = response.read()

weather_info = json.loads(data)

if weather_info ["cod"] == "404":
    print("City not found")
else:
    main_data = weather_info["main"]
    weather_data = weather_info["weather"][0]
    temp = main_data["temp"]
    pressure = main_data["pressure"]
    humidity = main_data["humidity"]
    weather_description = weather_data["description"]
      
      
# Step 9: Display the weather information
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")

