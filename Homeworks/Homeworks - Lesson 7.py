"""
1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
в) Посчитать среднее количество лет всех людей из списка.
"""
persons = [{"name": "John", "age": 42},
           {"name": "Jake", "age": 45},
           {"name": "Jordan", "age": 12},
           {"name": "Anton", "age": 12}]
age_persons = [person['age'] for person in persons]
young_persons = [person['name'] for person in persons if person['age'] == min(age_persons)]
print('Имя самого молодого человека:', young_persons)

name_persons = [len(person['name']) for person in persons]
max_name_persons = [person['name'] for person in persons if len(person['name']) == max(name_persons)]
print('Самое длинное имя:', max_name_persons)

middle_age = sum(age_persons) // len(age_persons)
print('Средний возраст:', middle_age)

"""
2) Даны два словаря my_dict_1 и my_dict_2.
а) Создать список из ключей, которые есть в обоих словарях.
б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
"""
my_dict_1 = {"Коржи": "Яйцо",
             "Крем": "50гр.",
             "Глазурь": "Масло"}

my_dict_2 = {"Начинка": "Молоко",
             "Сметана": "Сахар",
             "Глазурь": "Масло"}

intersection_list = list(set(my_dict_1).intersection(my_dict_2))
print(intersection_list)

difference_list = list(set(my_dict_1).difference(my_dict_2))
print(difference_list)

my_dict = {keys: my_dict_1[keys] for keys in difference_list}
print(my_dict)

list_unique_keys = list(set(my_dict_1).symmetric_difference(my_dict_2))

new_dict_2 = {keys: (my_dict_1 | my_dict_2)[keys] for keys in list_unique_keys}

new_dict_2.update({key: [my_dict_1[key], my_dict_2[key]] for key in intersection_list})

print(list_unique_keys)
print(new_dict_2)
