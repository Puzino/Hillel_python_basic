my_str = [1, 2, 3, 4, 5, 5, 4, 2, 1, 1, 2, 3]
my_list = []
str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
print(my_list)
