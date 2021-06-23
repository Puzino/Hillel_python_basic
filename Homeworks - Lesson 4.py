# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.
my_list = [100, 101, 5, 164, 1, 5, 4, 7, 78, 555, 468, 487]
for list in my_list:
    if list >= 100:
        print(list)

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.
my_list = [100, 101, 5, 164, 1, 5, 4, 7, 78, 555, 468, 487]
my_results = []
for list in my_list:
    if list >= 100:
        my_results.append(list)
print(my_results)

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)
my_list = [1, 5, 4, 7, 4, 8, 9, 6, 7]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)

# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.
value = input('Number: ')
try:
    value = float(value)
    result = value ** -1
except ValueError:
    print("Число не может быть приведено к типу float")
    result = 0
except ZeroDivisionError:
    print("На ноль делить нельзя!!")
    result = -1
print(result)

# 5) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и ПОМЕСТИТЬ их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))
my_string = '0123456789'
my_list = []
for symb1 in my_string:
    for symb2 in my_string:
        num = int(symb1 + symb2)
        my_list.append(num)
print(my_list)

# 6) Задание со "звёздочкой".
tmp_value = 5
while True:
    value = input("Введи число от 1 до 10: ")
    if value == str(tmp_value):
        print("Ура, угадал!")
        break
    elif value <= str(tmp_value):
        print(f'Попробуй число больше чем {value}')
    elif value >= str(tmp_value):
        print(f'Попробуй число меньше чем {value}')
