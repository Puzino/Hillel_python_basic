import random
import string

"""
1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
"""


def func_list_1(list_1):
    return [symbol[::-1] if not index % 2 else symbol for index, symbol in enumerate(list_1)]


my_list = ['hello', 'beautiful', 'world', 'goodbye', 'boring', 'job']

new_list = func_list_1(my_list)
print('1)-----------------------------')
print(new_list)
"""
2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
"""


def func_list_2(list_2):
    return [symbol for symbol in my_list if symbol[0].find('a') >= 0]


my_list = ['add', 'all', 'good', 'defence', 'avvv']
new_list = func_list_2(my_list)
print('2)-----------------------------')
print(new_list)
"""
3. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""


def func_list_3(list_3):
    return [value for index, value in enumerate(list_3) if 'a' in value]


my_list = ['asda', 'qwe', "asda", 'zxc', 'gfa', 'alll']
new_list = func_list_3(my_list)
print('3)-----------------------------')
print(new_list)
"""
4. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.
"""


def func_list_4(list_4):
    return [symbol for index, symbol in enumerate(list_4) if isinstance(symbol, str)]


my_list = [1, 2, 3, "11", "22", 33]
new_list = func_list_4(my_list)
print('4)-----------------------------')
print(new_list)

"""
5. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.
"""


def func_list_5(list_5):
    return [number for number in set(my_str) if my_str.count(number) == 1]


my_str = '122233334555567889'
new_list = func_list_5(my_str)
print('5)-----------------------------')
print(new_list)
"""
6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""


def func_list_6(my_str_1, my_str_2):
    return list(set(my_str_1).intersection(my_str_2))


my_str_1 = '1234qwerv'
my_str_2 = '123456qweterrte'
new_list = func_list_6(my_str_1, my_str_2)
print('6)-----------------------------')
print(new_list)
"""
7. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
"""


def func_list_7(my_str_1, my_str_2):
    return [number for number in set(my_str_1).union(my_str_2) if my_str_1.count(number) == 1 and my_str_2.count(number) == 1]


my_str_1 = '1233334555567889'
my_str_2 = '133334555567889'
new_list = func_list_7(my_str_1, my_str_2)
print('7)-----------------------------')
print(new_list)
"""
8. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.

Пример использования функции:
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
>>>miller.249@sgdyyur.com
"""


def create_email(list_1, list_2):
    return random.choice(list_1) + '.' + str(random.randint(100, 999)) + '@' + \
           ''.join(
               random.choice(string.ascii_lowercase) for count in range(0, random.randint(5, 7))) + '.' + random.choice(
        list_2)


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

e_mail = create_email(names, domains)
print('8)-----------------------------')
print(e_mail)
