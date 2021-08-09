"""
data.json - файл с данными о некоторых математиках прошлого.
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
4. Написать функцию сортировки по количеству слов в поле "text"
"""
import json


# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data


print(f'Json data: {read_json("data.json")}')


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Если фамилии нет, то использовать имя, например Euclid.


def split_name(path):
    dicts_list = read_json(path)
    for dict in dicts_list:
        splited_name = dict['name'].split(' ')
        dict['name'] = splited_name
    return dicts_list


def sort_by_last_name(last_name_dict):
    last_name = last_name_dict['name']
    last_name = last_name[-1]
    first_name = last_name_dict['name']
    first_name = first_name[0]
    return last_name, first_name


def join_name(path):
    sorted_by_last_name_list = sorted(split_name(path), key=sort_by_last_name)
    for dict in sorted_by_last_name_list:
        joined_name = ' '.join(dict['name'])
        dict['name'] = joined_name
    return sorted_by_last_name_list


print(f'Sorted by last name: {join_name("data.json")}')


# 3. Написать функцию сортировки по дате смерти из поля "years".


def split_year(path):
    dicts_list = read_json(path)
    for dict in dicts_list:
        splited_years = dict['years'].split(' ')
        dict['years'] = splited_years
        if dict['years'][-1] == 'BC.':
            dict['years'][-2] = f'-{dict["years"][-2]}'
            dict['years'].pop(-1)
    return dicts_list


def sort_by_year(year_dict):
    year = float(year_dict['years'][-1])
    return year


def join_year(path):
    sorted_by_year_list = sorted(split_year(path), key=sort_by_year)
    for dict in sorted_by_year_list:
        if float(dict['years'][-1]) < 0:
            dict['years'][-1] = dict['years'][-1].replace('-', '')
            dict['years'].append('BC.')
        joined_year = ' '.join(dict['years'])
        dict['years'] = joined_year
    return sorted_by_year_list


print(f'Sorted by last year: {join_year("data.json")}')


# 4. Написать функцию сортировки по количеству слов в поле "text"


def split_text(path):
    dicts_list = read_json(path)
    for dict in dicts_list:
        splited_text = dict['text'].split(' ')
        dict['text'] = splited_text
    return dicts_list


def join_text(path):
    sorted_by_words_number_list = sorted(split_text(path), key=lambda x: len(x.get('text')))
    for dict in sorted_by_words_number_list:
        joined_text = ' '.join(dict['text'])
        dict['text'] = joined_text
    return sorted_by_words_number_list


print(f'Sorted by words number in text field: {join_text("data.json")}')