# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому
# правилу: если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
value = 100
new_value = value // 2 if value < 100 else -1
print(new_value)

# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому
# правилу: если value меньше 100, то new_value равно 1, в противном случае - 0
value = 10
new_value = 1 if value < 100 else 0
print(new_value)

# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому
# правилу: если value меньше 100, то new_value равно True, в противном случае - False
value = 100
new_value = True if value < 100 else False
print(new_value)

# 4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
my_str = 'qwerty'
my_str = my_str.upper()
print(my_str)

# 5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
my_str = 'QWERTY'
my_str = my_str.lower()
print(my_str)

# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
my_str = 'qwer'
s = len(my_str)
n = 5
new_str = my_str * 2 if s < n else my_str
print(new_str)

# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
my_str = 'qwer'
s = len(my_str)
n = 5
back_str = my_str[::-1]
new_str = my_str + back_str if s < n else my_str
print(new_str)