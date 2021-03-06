"""
1. Дано целое число (int). Определить сколько нулей в этом числе.
"""
my_number = 101010101010110
str_my_number = str(my_number)
count_my_number = str_my_number.count('0')
print(count_my_number)

"""
2. Дано целое число (int). Определить сколько нулей в конце этого числа.
Например для числа 1002000 - три нуля
"""
my_number = 10020000
str_my_number = str(my_number)
print(len(str_my_number) - len(str_my_number.rstrip('0')))

"""
3. Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить
элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
"""
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

"""
4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
"""
my_list = [1, 2, 3, 4]
new_list = []
extend_new_list = new_list.extend(my_list)
my_extend_new_list = new_list.extend([my_list[0]][::-1])
pop_new_list = new_list.pop(0)
print(new_list)

"""
5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
"""
my_list = [1, 2, 3, 4]
first_element=my_list.pop(0)
my_list.append(first_element)
print(my_list)

"""
6. Дана строка в которой есть числа (разделяются пробелами).
Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
Для данного примера ответ - 133. (используйте split и проверку isdigit)
"""
my_str = "43 больше чем 34 но меньше чем 56"
word_list = my_str.split()
num_list = []
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
sum_num_list = sum(num_list)
print(sum_num_list)

"""
7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
"""
my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
l_limit_find = my_str.find(l_limit)
r_rlimit_find = my_str.rfind(r_limit)
sub_str = my_str[l_limit_find + 1:r_rlimit_find]
print(sub_str)

"""
8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
(используйте срезы длинны 2)
"""
my_str = 'abcde'
my_list = []
for index in range(0, len(my_str), 2):
    sub_str = my_str[index:index + 2]
    if len(sub_str) == 2:
        my_list.append(sub_str)
    else:
        sub_str = sub_str + '_'
        my_list.append(sub_str)
print(my_list)

"""
9. Дан список чисел. Определите, сколько в этом списке элементов,
которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
"""
print('9)-----------------------------------------------')
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
