# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и
# my_list_2 через один, начиная с my_list_1.
# a) кол-во эл-тов одинаковое
# б) кол-во эл-тов разное. Оставшиеся дописать в конец.

my_list_1 = [1, 2, 3, 4, ]
my_list_2 = [10, 20, 30, 40, 50]
my_result = []

min_len_lists = min(len(my_list_1), len(my_list_2))

for index in range(min_len_lists):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])

last_values_list_1 = my_list_1[min_len_lists:]
last_values_list_2 = my_list_2[min_len_lists:]

my_result = my_result + last_values_list_1 + last_values_list_2

print(my_result)

# id() - номер объекта в памяти
my_list = [1, 2, 3]
print(id(my_list))
my_list = [2, 3, 4, 5]
print(id(my_list))
my_list.append(6)
print(id(my_list))

my_list = [1, 2, 3]

result = []
print(id(result))

result = result + my_list
print(id(result))

result += my_list
print(id(result))

value = 10
value += 2
print(value)

value = 10
value = value + 2
print(value)

# генератор списков
folders = []
for digit in range(1, 21):
    folder = f"/tpm/{digit}"
    folders.append(folder)
print(folders)

folders = [f"/tpm/{digit}" for digit in range(1, 21) if not digit % 3]
print(folders)

symbols = [ord(symbol) for symbol in 'eyuioaи']
print(symbols)

alphabet = [chr(ord_index) for ord_index in range(ord("a"), ord("z") + 1)]
alphabet = "".join(alphabet)
print(alphabet)