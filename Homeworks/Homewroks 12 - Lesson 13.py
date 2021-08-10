"""
1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.


2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
Имя файла сделать параметром по умолчанию.
Заголовки csv файла:
Author, Quote, URL.
Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
"""
import requests
import random


def get_raw_quote(lang="ru"):
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "lang": lang,
              "key": random.randint(1, 999999)}
    response = requests.get(url, params=params)
    return response.json()


def get_quote(raw_quote):
    return raw_quote['quoteText']


def get_author(raw_quote):
    return raw_quote['quoteAuthor']


def get_int(key):
    for request_number in range(key):
        raw_quote = get_raw_quote()
        quote = get_quote(raw_quote)
        new_get_author = get_author(raw_quote)

        print([f'{quote} @{new_get_author}'])


new_get = get_int(5)
print(new_get)
