my_list = [2, 4, 1, 5, 3, 9, 0, 7, 21, 12521, 12, 21, 4, 15]
new_list = []
final_list = []
for index in range(len(my_list)):
    if index < len(my_list) - 2:
        sub_list = my_list[index:index + 3]
        new_list.append(sub_list)
        for index in range(len(new_list)):
            sub_list = new_list[index]
            if sub_list[1] > sub_list[0] + sub_list[2]:
                final_list.append(sub_list[1])
result = len(final_list)
print(final_list)
print(result)
