import requests
import json


name_book = str(input("Введіть ключові слова книги:"))
key = "AIzaSyCQbudW804Rq0PETDoGclkj-KhBMND41RU"

url = (f'https://www.googleapis.com/books/v1/volumes?q={name_book}+intitle:keyes&key={key}')

book = requests.get(url)

print("\n", "Заголовок книги: ", json.loads(book.text)['items'][0]['volumeInfo']['title'], "\n")
print("Автори цієї книги: ", json.loads(book.text)['items'][0]['volumeInfo']['authors'], "\n")
print("Кількість сторінок: ", json.loads(book.text)['items'][0]['volumeInfo']['pageCount'], "\n")
print("Уривок тексту з ключовими словами які ви ввели: ", json.loads(book.text)['items'][0]['searchInfo']['textSnippet'], "\n")