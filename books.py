import requests
import json


name_book = input("Введіть назву книжки:")
book = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={name_book}+intitle:keyes&key=AIzaSyCQbudW804Rq0PETDoGclkj-KhBMND41RU')
json = url.json()

print(json)