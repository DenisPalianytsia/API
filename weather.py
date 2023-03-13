import requests
import json


city = input("Введіть назву міста:")
api_key = "5a3971056502f889afa15f55f7e33ee3"
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
result = requests.get(url)
json = result.json()

print(json)