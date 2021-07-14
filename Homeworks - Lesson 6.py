"""
1. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
Задание сделать с использованием enumerate или range.
"""
my_list = ['qwe', 'rty', 'uio']
result = []
for index, value in enumerate(my_list):
    if not index % 2:
        result.append(value[::-1])
    else:
        result.append(value)
print(result)

"""
2. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list у которых первый символ - буква "a".
"""

my_list = ['add', 'all', 'good', 'defence']
new_list = [symbol for symbol in my_list if symbol[0].find('a') >= 0]
print(new_list)

"""
3. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""
my_list = ['asda', 'qwe', "asda", 'zxc', 'gfa', 'alll']
result = []
for index, value in enumerate(my_list):
    if 'a' in value:
        result.append(value)

print(result)

"""
4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
Например [1, 2, 3, "11", "22", 33]
Создать новый список в который поместить только строки из my_list.
"""
my_list = [1, 2, 3, "11", "22", 33]
result = []
for index, symbol in enumerate(my_list):
    if isinstance(symbol, str):
        result.append(symbol)

print(result)

"""
5. Дана строка my_str. Создать список в который поместить те символы из my_str,
которые встречаются в строке ТОЛЬКО ОДИН раз.
"""
my_str = '122233334555567889'
my_set_str = set(my_str)
my_list = []
for number in my_set_str:
    if my_str.count(number) == 1: my_list.append(number)
print(my_list)

"""
6. Даны две строки. Создать список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""
my_str_1 = '123qwerrr'
my_str_2 = '123456qweterte'
set_my_str_1 = set(my_str_1)
set_my_str_2 = set(my_str_2)
my_list = []
intersection = set_my_str_1.intersection(set_my_str_2)
extend_my_list = my_list.extend(intersection)
print(my_list)

"""
7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
но в каждой ТОЛЬКО ПО ОДНОМУ разу.
"""
my_str_1 = '1233334555567889'
my_str_2 = '1233334555567889'
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
my_list = []
union = my_set_1.union(my_set_2)
for number in union:
    if my_str_1.count(number) == 1 and my_str_2.count(number) == 1: my_list.append(number)
print(my_list)

"""
8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
Фамилия
Имя
Возраст
Проживание
    Страна
    Город
    Улица
Работа
    Наличие
    Должность
"""
human = {"Имя": "Андрей",
         "Возраст": "21",
         "Проживание": {"Страна": "Украина", "Город": "Днепр", "Улица": "Гагарина"},
         "Работа": {"Наличие": "Есть", "Должность": "Инспектор"}
         }
print(human)

"""
9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
придумать и указать граммы для продуктов):
Составляющие
    Коржи
        Мука
        Молоко
        Масло
        Яйцо
    Крем
        Сахар
        Масло
        Ваниль
        Сметана
    Глазурь
        Какао
        Сахар
        Масло
"""
tortik = {"Коржи": {"Мука": "100 гр.", "Молоко": "1 л.", "Масло": "50 гр.", "Яйцо": "2 шт."},
          "Крем": {"Сахар": "100 гр.", "Масло": "50 гр.", "Ваниль": "10 гр.", "Сметана": "50 гр."},
          "Глазурь": {"Какао": "50 гр.", "Сахар": "50 гр.", "Масло": "50 гр."}}
print(tortik)
