import os

# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""
# def create_domains(domains):


"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""


# def create_name(path):
#     with open(path, 'r') as txt_file:
#         data = txt_file.readlines()
#
#     for line in data:
#         print(line.split("\t"))
#
#
# new_list = create_name("C:/Users/admin/Documents/GitHub/Hillel/names.txt")
# print(new_list)
"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""
def create_authors(path):
    with open(path, 'r') as txt_file:
        data = txt_file.readlines()

    for line in data:
        print(line.split(" - "))

new_list = create_authors("C:/Users/admin/Documents/GitHub/Hillel/authors.txt")
print(new_list)