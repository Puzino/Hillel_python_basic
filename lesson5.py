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

my_str = 'blablacarblablacarblablacarblablacar'
my_symbol = 'bla'
my_symbol_count = my_str.count(my_symbol)
for index in range(my_symbol_count):
    print(my_symbol)