# json, csv
# импорт из файла
# assert
import json
from lesson11_csv import read_from_csv

def write_json(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data


data_list = [1, 2, 3, 4, 5]
data_dict = {"name": "John",
             "age": 13,
             "job": {"title": "Data Ingener",
                     "price": "1000$"}}
# data_dumps = json.dumps(data)
# print(data_dumps, type(data_dumps))

filename = "data_dict.json"
write_json(filename, data_dict)
data = read_json(filename)
print(data, type(data))


filename = "new_data_2.csv"
new_data = read_from_csv(filename)
print(new_data)