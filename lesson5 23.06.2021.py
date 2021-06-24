# tmp_value = 5
# go_game = True
# text_message = input('Введи число от 1 до 10: ')
# while go_game:
#     try:
#         value = int(input(text_message))
#         if tmp_value > value:
#             text_message = 'Попробуй больше '
#         elif tmp_value < value:
#             text_message = 'Попробуй меньше '
#         else:
#             go_game = False
#             print('Ура, угадал!.')
#     except ValueError:
#         text_message = 'Введи число от 1 до 10: '

# value = input("Введи число от 1 до 10: ")
# if value == str(tmp_value):
#     print("Ура, угадал!")
#     break
# elif int(value) <= int(tmp_value):
#     value = input("Попробуй число больше: ")
#     print(f'Попробуй число больше чем {value}')
# elif int(value) >= int(tmp_value):
#     value = input("Попробуй число меньше: ")
#     print(f'Попробуй число меньше чем {value}')

# my_str = 'blablacar'
# my_symbol = 'bla'
# my_symbol_count = my_str.count(my_symbol)
# for index in range(my_symbol_count):
#     print(my_symbol)

# my_str = 'bla BLA car'
# my_str = my_str.lower()
# symbols_heap = []
# for symbol in my_str:
#     if symbol not in symbols_heap:
#         symbols_heap.append(symbol)
# res_len = len(symbols_heap)
# print(res_len)

# my_str = 'qwerty'
# my_list = []
# for index in range(len(my_str)):
#     if not index % 2:
#         symbols = my_str[index]
#         my_list.append(symbols)
#
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbols)
#
# print(my_list)


# my_str = 'qwerty'
# my_list = []
# str_index = [0, 1, 2, 3, 3, 4, 5, 0, 4, 4, 1, 3, 3, 4]
#
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

my_number = 1523478906
digit_count = len(str(my_number))
print(digit_count)

# ord("") #Проверяет номер числа
# chr() #Проверка числа
#
# number_str = str(my_number)
# max_symbol = max(number_str)
# print(max_symbol)
#
# test_list = [1, 2, 3, 4]
# print(max(test_list))

# number_str = str(my_number)
# new_number_str = number_str[::-1]
# new_number = int(new_number_str)
# print(new_number)


#Сложить для себя в одну строку
# number_str = str(my_number)
# sorted_number_symbols_list = sorted(number_str, reverse=True)
# new_number_str = ''.join(sorted_number_symbols_list)
# new_number = int(new_number_str)
# print(new_number)



# my_list = [1, 2, 3, 4, 5, -6, 7, 8]
# my_str = 'qwertyuiopasdfghjklzxcvbnm'
# sorted_list = sorted(my_str)
# print(sorted_list)



