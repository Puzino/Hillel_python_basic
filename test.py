# my_str_1 = '1233334555567889'
# my_str_2 = '1233334555567889'
# set_my_str_1 = set(my_str_1)
# set_my_str_2 = set(my_str_2)
# intersection = set_my_str_1.intersection(set_my_str_2)
# counter = {}
#
# for elem in intersection:
#     counter[elem] = counter.get(elem, 0) + 1
#
# doubles = {element: count for element, count in counter.items() if count > 1}
#
# print(doubles)

my_list = [3, 10, 10, 2, "2", 2, 3, 3, 3, 3, 3, 3, 3]
# my_list_unique = list(set(my_list)) #- убирает дубли
# my_set = set(my_list)
# print(my_set)
# my_list_unique = list(my_set)
# print(my_list_unique)
word_list = my_list.split()
num_list = []
for word in my_list:
    if word.isnumeric():
        num_list.append(int(word))

print(num_list)