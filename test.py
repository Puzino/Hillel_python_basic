my_dict_1 = {"Коржи": "Яйцо",
             "Крем": "50гр.",
             "Глазурь": "Масло"}

my_dict_2 = {"Начинка": "Молоко",
             "Сметана": "Сахар",
             "Глазурь": "Масло"}

# intersection_list = list(set(my_dict_1).intersection(my_dict_2))
# print(intersection_list)
#
difference_list = list(set(my_dict_1).difference(my_dict_2))
print(difference_list)

my_dict = {keys: my_dict_1[keys] for keys in difference_list}
print(my_dict)