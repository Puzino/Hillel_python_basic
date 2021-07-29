import os
import string
import re

# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""

# def create_domains(domains):
#     with open(domains, "r") as txt_file:
#         domain = txt_file.readlines()
#     return [re.sub('[.\\n]', '', word) for word in domain]
#
#
# new_list = create_domains('domains.txt')
# print(new_list)

"""
сделалллл!!!!!!!!!!!!
"""

"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""

# def create_name(path):
#     with open(path, 'r') as txt_file:
#         path = txt_file.readlines()
#     return [line.split()[1] for line in path]
#
#
# new_list = create_name("names.txt")
# print(new_list)

"""
сделалллл!!!!!!!!!!!!
"""

"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""
"""
не сделалллл!!!!!!!!!!!!
"""

def create_authors(path):
    with open(path, 'r') as txt_file:
        path = txt_file.readlines()
    return {"date_original": line.split(' - ')[0] for line in path}


new_list = create_authors("authors.txt")
print(new_list)
