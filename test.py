import random
import string


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


print(random_char(7) + "@gmail.com")
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
print('9)-----------------------------')
print(e_mail)
