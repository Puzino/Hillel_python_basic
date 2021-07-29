# 1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

# 2. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 1 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.
import random
import string


def generate_string(min_limit=50, max_limit=100):
    len_str = random.randint(min_limit, max_limit)
    res_str = "".join([random.choice(string.ascii_lowercase) for _ in range(len_str)])
    return res_str


def choice_transform(word):
    word = word.capitalize()
    return word


def fransform_str_by_words(some_str):
    new_words = []
    words = some_str.split()
    for word in words:
        word = choice_transform(word)
        new_words.append(word)
    return " ".join(new_words)


def insert_spaces(some_str):
    go_jump = True
    total_index = 0
    some_list = list(some_str)
    while go_jump:
        jump_index = random.randint(2, 11)
        current_index = total_index + jump_index
        if current_index < len(some_list):
            some_list[current_index] = " "
            total_index += jump_index
        else:
            go_jump = False
    return "".join(some_list)


def transform_str(some_str):
    some_str = insert_spaces(some_str)
    some_str = fransform_str_by_words(some_str)
    return some_str


rand_str = generate_string()
tr_str = transform_str(rand_str)
print(tr_str)