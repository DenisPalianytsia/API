import requests
import json


location = input("Введіть локацію:")
latitude = input("Введіть широту:")
longitude = input("Введіть довготу:")
url = f"https://api.yelp.com/v3/businesses/search?location={location}&latitude={latitude}&longitude={longitude}&sort_by=best_match"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer yGHUwfxURbELVUAES2eWK9wK5oS1eUUlIT80-WStwx2KAGSJ4NyIGn-cC9NsHv8qO3ffm_pCyP3PqIV4pMoruUd2nhZ0SkL3PYNrE0aXyq-iJOxTZxBBhbVdIvEOZHYx"
}

response = requests.get(url, headers=headers)

print(response.text)