# my_list = [1, 2, 3]
# new_list = [my_list.copy(), my_list.copy(), my_list.copy()]
# print(new_list)
# new_list[0].append(4)
# print(my_list)
# print(new_list)

## ДЗ*  давать подсказки типа: "Попробуй больше", "Попробуй меньше"

# tmp_value = 5
# go_game = True
# text_message = "Введи число от 1 до 10"
# while go_game:
#     try:
#         value = int(input(text_message))
#         if tmp_value > value:
#             text_message = "Попробуй больше"
#         elif tmp_value < value:
#             text_message = "Попробуй меньше"
#         else:
#             go_game = False
#             print("Ура, угадал!")
#     except ValueError:
#         text_message = "Введи число от 1 до 10"

"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
my_str = "blablacarblablacar"
my_symbol = "bla"

my_symbol_count = my_str.count(my_symbol)
print(my_symbol_count)


"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
res_msg = f"{my_symbol}\n" * my_symbol_count
print(res_msg.strip())

for _ in range(my_symbol_count):
    print(my_symbol)

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
my_str = my_str.lower()
symbols_heap = []
for symbol in my_str:
    if symbol not in symbols_heap:
        symbols_heap.append(symbol)
res_len = len(symbols_heap)
print(res_len)


"""
# 4)
# Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str, 
# которые стоят на четных местах в строке (считаем с 0)
# """
# my_str = "qwerty"
# my_list = []
# # for index in range(len(my_str)):
# #     if not index % 2:
# #         symbol = my_str[index]
# #         my_list.append(symbol)
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list)

"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
my_str = "qwerty"
my_list = []
str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
print(my_list)

"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""
my_number = 7812481234125126354123641275923854103418268
digit_count = len(str(my_number))
print(digit_count)


"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""

number_str = str(my_number)
max_symbol = max(number_str)
print(max_symbol)

test_list = [1, 2, 3, -4]
print(max(test_list))


"""
10)
Дано целое число. Составить число (int) с цифрами в обратном порядке.
"""
number_str = str(my_number)
new_number_str = number_str[::-1]
new_number = int(new_number_str)
print(new_number)

new_number = int(str(my_number)[::-1])
print(new_number)

"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""
number_str = str(my_number)
sorted_number_symbols_list = sorted(number_str)
new_number_str = ''.join(sorted_number_symbols_list)
new_number = int(new_number_str)
print(new_number)
my_list = [1, 2, 5, 3, -8, 4]
my_str = 'qwerty'
sorted_list = sorted(my_str)
print(sorted_list)