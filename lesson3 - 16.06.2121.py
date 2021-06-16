# value = 13
# if not value % 2 and not value % 3:
#     print('Делится на 2 и на 3')
# elif not value % 2:
#     print('Делится на 2')
# elif not value % 3:
#     print('Делится на 3')

#проверка на верно или не верно(да, нет)
# value = 'abc'
# new_value = bool(value)
# print(new_value)


# Тернарный оператор
# my_int = 100
# my_int = my_int // 2 if my_int > 10 else -1 # Тернарный оператор
# print(my_int)

# number = 12346545674798798713434
# print(len(str(number))) #Считает количество чифр, не работает со строкой = нужно перевести цифры в строку

# my_str = "1233454677890123"
# # index = 1
# # print(my_str[index])
#
# # Срез(Срезает вписанное количество символов которое пишется через двоеточие)
# new_str = my_str[1:3] #от(включая) до (невключая)
# shag_str = my_str[1:3:2] #от:до:шаг
#
# print(new_str)

name = 'Jhon'
age = 23

hello_message = f'Знакомтесь это, {name} ему {age}'
print(hello_message)