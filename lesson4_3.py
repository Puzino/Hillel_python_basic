test_str = "qwErty!@#$%^aksufhlaszv;aosUghfliagzb kj,ycf"
result = []
for symbol in test_str:
    if symbol.lower() not in "eyuioa" and symbol.isalpha():
        # print(f"symbol: {symbol}")
        result.append(symbol)
print(result)

join_str = "".join(result)
print(join_str)

split_str = list(test_str)
print(split_str)



# tuple - кортеж - неизменяемый тип
# list - список - изменяемый тип

my_tuple = (1, 2, "tuple", (-1, 0), None)
print(type(my_tuple), my_tuple)

my_list = [1, 2, "list", (-1, 0), None]
print(type(my_list), my_list)

index = -1
my_tuple = list(my_tuple)
my_tuple[index] = 'NEW_VALUE'
my_tuple = tuple(my_tuple)
my_list[index] = 3
value_tuple = my_tuple[index]
value_list = my_list[index]
print(value_tuple, value_list)
print(type(my_list), my_list)
# срезы как в строках

# приведение к типам
new_list = list(my_tuple)
new_tuple = tuple(my_list)
print("new_list",type(new_list), new_list)
print("new_tuple", type(new_tuple), new_tuple)

new_list = []

new_list.append('first')
new_list.append('second')
new_list.append([1,3,5])
last_value = new_list.pop()
print(new_list)
print(last_value)