# if
# if условие:
#     блок если ДА
# else:
#     блок если НЕТ
#
my_bool = False
value = str(my_bool)
if value:
    print(value)
print("The end")

value = 15
if value == 4:
    print("!!!!")
    print(value * 3)
    new_value = "asd" * value
    print(new_value)
else:
    print("Else case")

print("The end")

value = 15

if not value % 2 and not value % 3:
    print("Число делится и на 2 и на 3 - т.е. на 6")
elif not value % 2:
    print("Число делится только на 2")
elif not value % 3:
    print("Число делится только на 3")

my_str = "qwerty"
my_int = 9
if 'r' in my_str:
    new_str = my_str * 2
else:
    new_str = my_str

new_str = my_str * 2 if 'r' in my_str else my_str

new_int = my_int // 2 if my_int > 10 else -1
print(new_str)