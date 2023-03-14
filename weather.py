import requests
import json


city = str(input("Введіть назву міста: "))
api_key = "e4802e1ebecfffb4ed53e0c63027be2e"
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
result = requests.get(url)

print(result.text)