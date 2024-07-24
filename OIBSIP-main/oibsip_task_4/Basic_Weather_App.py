import requests
import json


def get_weather(city):
    api_key = '271d1234d3f497eed5b1d80a07b3fcd1'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(base_url)
    weather_data = response.json()
    
    if weather_data['cod'] != '404':
        main = weather_data['main']
        wind = weather_data['wind']
        weather_desc = weather_data['weather'][0]['description']
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        wind_speed = wind['speed']
        
        print(f"Temperature: {temperature}°C")
        print(f"Weather Description: {weather_desc}")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City Not Found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
