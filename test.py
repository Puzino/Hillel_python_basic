my_str_1 = '1233334555567889'
my_str_2 = '1233334555567889'
set_my_str_1 = set(my_str_1)
set_my_str_2 = set(my_str_2)
intersection = set_my_str_1.intersection(set_my_str_2)
counter = {}

for elem in intersection:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)