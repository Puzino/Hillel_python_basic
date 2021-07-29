import csv


def write_to_csv(filename, data, delimiter=","):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
        return data

filename = "data.csv"
# data_2 = [[1, 2, 3], [4, 5, 6], [12, 13, 14]]
# write_to_csv(data=data_2, filename=filename)  #  именованная передача аргументов
# write_to_csv(filename, delimiter=";", data=data_2)  # позиционная передача аргументов

new_data = read_from_csv(filename)

print("---->", new_data)

new_data[0].append("Sum")
for row in new_data[1:]:
    row.append(int(row[-2]) + int(row[-1]))

# new_data.append([100,200,300])
write_to_csv(data=new_data, filename="new_data.csv")