import requests
import json


city = "Kyiv"
api_key = "e4802e1ebecfffb4ed53e0c63027be2e"
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
result = requests.get(url)

print(json.loads(result.text))