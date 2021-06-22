# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.
# my_list = [100, 101, 5, 164, 1, 5, 4, 7, 78, 555, 468, 487]
# for i in my_list:
#     if i >= 100:
#         print(i)

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.
# my_list = [100, 101, 5, 164, 1, 5, 4, 7, 78, 555, 468, 487]
# my_results = []
# for i in my_list:
#     if i >= 100:
#         my_results.append(i)
# print(my_results)

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)
# my_list = [1, 5, 4, 7, 4, 8, 9]
# if len(my_list) < 2:
#     my_list.append(0)
#     print(my_list)
# elif len(my_list) >= 2:
#     my_list.append(my_list[5] + my_list[6])
#     print(my_list)
# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.
# value = input('Number: ')
# try:
#     value = float(value)
#     result = value ** -1
# except ValueError:
#     print("Число не может быть приведено к типу float")
#     result = 0
# except ZeroDivisionError:
#     print("На ноль делить нельзя!!")
#     result = -1
# print(result)

# 6) задание со звёздочкой.
# tmp_value = 5
# while True:
#     value = input("Введи число от 1 до 10: ")
#     if str(tmp_value) == value:
#         print("Ура, угадал!")
#         break
#     elif value <= str(4):
#         print(f'Попробуй число больше чем {value}')
#     elif value >= str(6):
#         print(f'Попробуй число меньше чем {value}')
