# Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. 

import requests
import json
import sys


api_key = "a3c37af4e9d9f8762841f8388905daa0"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name



response = requests.get(complete_url)

x = response.json()



if x["cod"] != "404":
    
       
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
    
        # print following values
        print("wheather report for " + city_name)
        print(" Temperature (in kelvin unit) = " +
            str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
            str(current_pressure) +
            "\n humidity (in percentage) = " +
            str(current_humidity) +
            "\n description = " +
            str(weather_description))

else:
    print(" City Not Found ")












