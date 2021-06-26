# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# my_number = 101010101010101010101010101010000
# str_my_number = str(my_number)
# count_my_number = str_my_number.count('0')
# print(count_my_number)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
# my_number = 10020000
# str_my_number = str(my_number)
# print(len(str_my_number) - len(str_my_number.rstrip('0')))


# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list_1 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
my_list_2 = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]
my_result = []
for index_1 in my_list_1[::2]:
    my_result.append(index_1)
for index_2, symbol in enumerate(my_list_2):
    if index_2 % 2:
        my_result.append(symbol)
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
# my_list_1 = [1, 2, 3, 4]
# my_result = []
# my_result.append(my_list_1 + my_list_1[1::-1])
# print(my_result)
