"""
Библиотеки пайтон
"""
import string
import random
# from random import randint
# import random as rnd
value = random.randint(10, 20)
my_list = [1, 2, 3, 10, 20, 30]
choice_from_list = random.choice(my_list)
new_list = my_list.copy()
random.shuffle(my_list)
print(my_list, new_list)
print(choice_from_list)
print(value)

print(string.ascii_letters)