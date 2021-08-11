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
import csv


def get_raw_quote(how_quotes):
    text_list = []
    while len(text_list) < how_quotes:
        url = 'http://api.forismatic.com/api/1.0/'
        params = {'method': 'getQuote',
                  'format': 'json',
                  'lang': 'ru',
                  'key': random.randint(1, 999999)}
        responce = requests.get(url, params=params)
        quote_json = responce.json()
        if not quote_json['quoteAuthor'] == '':
            list_quote = [quote_json['quoteAuthor'], quote_json['quoteText'], quote_json['quoteLink']]
            text_list.append(list_quote)
    return text_list


def write(file_csv, data):
    with open(file_csv, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Author', 'Quote', 'URL'])
        writer.writerows(sorted(data, key=lambda x: x[0]))


file_quotes_csv = 'quotes.csv'
list_author_quote_url = get_raw_quote(5)
write(file_quotes_csv, list_author_quote_url)
