import requests
from pprint import pprint 

API_KEY =''

city = input ('Enter a City :  ')

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city + "&appid="+API_KEY

weather_data =  requests.get(base_url).json()

pprint(weather_data)