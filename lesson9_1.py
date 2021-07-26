# with open("lesson10.py", "r") as py_file:
#     data = py_file.readlines()
#
# print(data, type(data))
#
# data.append("# FINISH\n")
# with open("lesson10_new.py", "w") as py_file:
#     py_file.writelines(data)

with open("Homeworks/names.txt", "r") as txt_file:
    data = txt_file.readlines()

for line in data:
    if len(line) > 32:
        print(line.split("\t"))