################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def create_file(path, symbol):
    filename = f"{path}/{symbol}.txt"
    with open(filename, 'w') as txt_file:
        txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_files_in_dir(path):
    for letter in string.ascii_lowercase:
        create_file(path, letter)


def get_tanos_click(path):
    files = os.listdir(path)
    files = list(set(files))[:len(files) // 2]
    for file in files:
        os.remove(os.path.join(path, file))


# create_dir("alphabet")
create_files_in_dir("alphabet")
get_tanos_click("alphabet")