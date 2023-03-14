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

restorans = requests.get(url, headers=headers)

print("Ім'я ресторану: ", json.loads(restorans.text)['businesses'][0]['name'], "\n")
print("Картинка ресторану: ", json.loads(restorans.text)['businesses'][0]['image_url'], "\n")
print("Місцезнаходження ресторану: ", json.loads(restorans.text)['businesses'][0]['location'], "\n")
print("Номер телефону ресторану: ", json.loads(restorans.text)['businesses'][0]['phone'], "\n")