"""
3. Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить
элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
"""
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50]
# my_result = []
# for index in range(len(my_list_1)):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)

#
# my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list_2 = [10, 20, 30, 40, 50]
# min_len_list = min(len(my_list_1), len(my_list_2))
# my_result = []
# for index in range(min_len_list):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# last_values_list_1 = my_list_1[min_len_list:]
# last_values_list_2 = my_list_2[min_len_list:]
# my_result = my_result + last_values_list_1 + last_values_list_2
# print(my_result)

"""
Функция "ID"
"""

# my_list = [1, 2, 3]
# print(id(my_list))
# my_list = [2, 3, 4, 5]
# print(id(my_list))
# my_list.append(6)
# print(id(my_list))

# my_list = [1, 2, 3]
# result = []
# print(id(result))
# my_list = result + my_list
# print(id(result))
#
# my_list += my_list
# print(id(result))


"""
Генератор списков - [что? цикл условие]
"""
# folders = []
# for digit in range(1, 20):
#     folder = f'/tmp/{digit}'
#     folders.append(folder)
# print(folders)

# folders = [f'/tmp/{digit}'

# symbol = [ord(symbol) for symbol in 'eyunioa']
# print(symbol)

# alphabet = [chr(ord_index) for ord_index in range(ord('a'), ord('z') + 1)]
# alphabet = ''.join(alphabet)
# print(alphabet)

"""
Множество - set - не сохраняет порядок, все элементы уникальные 
"""
# my_list = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# # my_list_unique = list(set(my_list))
# my_set = set(my_list)
# print(my_set)
# my_list_unique = list(my_set)
# print(my_list_unique)
#
# new_set = {1, 2, 3, 4, 5, 6, 6, 66, 7, 8, 8, 8, 54, 54}
# print(new_set)

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
# my_str = "bla BLA car"
# my_str = my_str.lower()
# res_len = len(set(my_str))
# print(res_len)


# my_str = 'qqqqqqqqqwwweeeeeeeeeeeeeeerty'
# for symbol in set(my_str):
#     print(symbol, my_str.count(symbol))

# my_str_1 = 'qwerty'
# my_str_2 = 'qweasd'
# my_set_1 = set(my_str_1)
# my_set_2 = set(my_str_2)
# intersection = my_set_1.intersection(my_set_2)
# union = my_set_1.union(my_set_2)
# difference = my_set_1.difference(my_set_2)
# print(intersection)
# print(union)
# print(difference)

"""
Словарь (dict) - не гарантирует порядок, все ключи уникальные ( словарь = {"ключ": [1, 2],} )
остаётся последнее значение
ключи - это любые не изменяемые объекты (строка, кортеж, число)
"""
# triangle = [[1, 1], [2, 3], [4, -2]]
# print(triangle[1][1])

key = {1,2,'qwe'}
test_dict = {1: 'qwerty',
             '11': 12,
             key: 'test'}
print(test_dict)

# triangle = {'A': {'x': 1, 'y': 1},
#             'B': {'x': 2, 'y': 3},
#             'C': {'x': 4, 'y': -2}}
# print(triangle['B']['x'])
# print(triangle)
#
#
#
