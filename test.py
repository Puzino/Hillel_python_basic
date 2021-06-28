my_str = "43 больше чем 34 но меньше чем 56"
# вариант 1
len_my_str = len(my_str)
integ = []
num = 0
while num < len_my_str:
    my_str_int = ''
    num_1 = my_str[num]
    while '0' <= num_1 <= '9':
        my_str_int += num_1
        num += 1
        if num < len_my_str:
            num_1 = my_str[num]
        else:
            break
    num += 1
    if my_str_int != '':
        integ.append(int(my_str_int))
print(integ)
# вариант 2
num_list = []
num = ''
for char in my_str:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
print(num_list)

# вариант 3
word_list = my_str.split()
num_list = []
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
sum_num_list = sum(num_list)
print(sum_num_list)