import os
import re

# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""


def create_domains(domains):
    with open(domains, "r") as txt_file:
        domain = txt_file.readlines()
    return [re.sub('[.\\n]', '', word) for word in domain]


new_list = create_domains('domains.txt')
print(f'Domains: {new_list}')

"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""


def create_name(path):
    with open(path, 'r') as txt_file:
        path = txt_file.readlines()
    return [line.split()[1] for line in path]


new_list = create_name("names.txt")
print(f'Last names: {new_list}')

"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""

month = {'January': '01',
         'February': '02',
         'March': '03',
         'April': '04',
         'May': '05',
         'June': '06',
         'July': '07',
         'August': '08',
         'September': '09',
         'October': '10',
         'November': '11',
         'December': '12'}


def get_original_dates(file_name: str) -> list:
    dates_original_list = []
    file_lines_list = create_name(file_name)
    for line in file_lines_list:
        line = line.split(' - ')
        for item in line:
            if re.search(r"[0-31][a-z]{2}\s.+", item):
                dates_original_list.append(item)
    return dates_original_list


def get_date_modified(file_name: str):
    dates_original_list = get_original_dates(file_name)
    dates_modified_list = []
    for date in dates_original_list:
        date = date.split(' ')
        day_of_the_month = date[1]
        day_of_the_month = day_of_the_month.rstrip('ndrsth')
        if int(day_of_the_month) < 10:
            modified_day_of_the_month = f'0{day_of_the_month}'
        else:
            modified_day_of_the_month = day_of_the_month
        modified_month = month[date[1]]
        if len(date) == 3:
            year = date[2]
            modified_date = f'{modified_day_of_the_month}/{modified_month}/{year}'
        else:
            modified_date = f'{modified_day_of_the_month}/{modified_month}'
        dates_modified_list.append(modified_date)
    return dates_original_list, dates_modified_list


def create_final_dicts_list(file_name: str) -> list:
    final_dicts_list = []
    date_lists_tuple = get_date_modified(file_name)
    dates_original_list = date_lists_tuple[0]
    dates_modified_list = date_lists_tuple[1]
    for index, date in enumerate(dates_original_list):
        dates_dict = {'date_original': date, 'date_modified': dates_modified_list[index]}
        final_dicts_list.append(dates_dict)
    return final_dicts_list


result_dates_list = create_final_dicts_list('authors.txt')
print(f'Dates list: {result_dates_list}')
