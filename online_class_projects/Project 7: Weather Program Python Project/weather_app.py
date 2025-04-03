# Project 7: Weather Program Python Project

 # Import requests module for API call
import requests

city_name = input("Enter City Name: ") # Get city name from user

# OpenWeather API key
API_key = '7f3660fa537bb088b13d5a4ab9e1e7e4' 

# Create API URL with city name and API key
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

# Send API request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert response to JSON format
    # Print weather condition
    print('Weather is ', data['weather'][0]['description'])
     # Print current temperature
    print('Current Temperature is', data['main']['temp'])
    
    print('Current Temperature Feels like is', data['main']['feels_like'])
    print('Humidity is', data['main']['humidity'])


# output1:

# Enter City Name: Karachi
# Weather is  clear sky
# Current Temperature is 28.9
# Current Temperature Feels like is 31.02
# Humidity is 61


# output2:

# Enter City Name: Agra
# Weather is  scattered clouds
# Current Temperature is 29.27
# Current Temperature Feels like is 27.8
# Humidity is 24





