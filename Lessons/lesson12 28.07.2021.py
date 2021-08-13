"""Сортировка"""

# my_list = [12, 3, 4, 5, 6, -7, 87]
# sorted_list = sorted(my_list, reverse=True)
#
# print(sorted_list)

# def sort_by_len_end_name(name):
#     return len(name), name
import re

# my_str_list = ['John', 'Tim', 'Max', 'Jack']  # по алфавиту
# sorted_str_list = sorted(my_str_list)
# print(sorted_str_list)

# sorted_str_list = sorted(my_str_list, key=sort_by_len_end_name)  # по длине
# print(sorted_str_list)

# def sort_by_price(price_dict):
#     price = price_dict['Price']
#     name = price_dict['product']
#     return price, name
#
#
# price_list = [{'product': 'Milk', 'Price': 23},
#               {'product': 'ice-cream', 'Price': 18},
#               {'product': 'meat', 'Price': 120},
#               {'product': 'coca-cola', 'Price': 10},
#               {'product': 'pepsi-cola', 'Price': 10}
#               ]
#
# sorted_price_list = sorted(price_list, key=sort_by_price)
# print(sorted_price_list)


# регулярные выражения
# my_string = 'asdiuajsdiasdiaj1323123.123123sdioajs 127.0.0.1 sadasdasdasdasdeiwrg aisjdoaisdjoia 200.123.123.22:12345 asdasdasd'
# template = r'\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}.\d{4,5}' #просто цифровые группы
# result = re.findall(template, my_string)
# print(result)

import random
import string


def generate_string(min_limit=50, max_limit=100):
    len_str = random.randint(min_limit, max_limit)
    res_str = ''.join([random.choice(string.ascii_lowercase) for _ in range(len_str)])
    return res_str


def choise_transform(word):
    word = word.capitalize()
    return word


def transform_str_by_words(some_str):
    new_words = []
    words = some_str.split()
    for word in words:
        word = choise_transform(word)
        new_words.append(word)
    return ' '.join(new_words)


def insert_spaces(some_str):
    go_jump = True
    total_index = 0
    some_list = list(some_str)
    while go_jump:
        jump_index = random.randint(2, 11)
        current_index = total_index + jump_index
        if current_index < len(some_list):
            some_list[current_index] = ' '
            total_index += jump_index
        else:
            go_jump = False
    return ''.join(some_list)


def transform_str(some_str):
    some_str = insert_spaces(some_str)
    some_str = transform_str_by_words(some_str)
    return some_str


rend_str = generate_string()
tr_str = transform_str(rend_str)
print(tr_str)
