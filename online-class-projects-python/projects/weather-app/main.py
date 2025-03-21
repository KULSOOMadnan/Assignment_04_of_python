import requests
from pprint import pprint 

API_KEY ='2a091fed0ea840af167b65726723d0b0'

city = input ('Enter a City :  ')

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city + "&appid="+API_KEY

weather_data =  requests.get(base_url).json()

pprint(weather_data)