my_list_1 = ['12', 'b', 2, 'dd', ['qwe', 121]]
my_list_2 = ['qq', 10, 'x', 'kl', 45, 12.23]
result = []
for index, symbol in enumerate(my_list_1):
    if not index % 2:
        result.append(symbol)
for index, symbol in enumerate(my_list_2):
    if index % 2:
        result.append(symbol)
print(result)