import csv


def read_dict_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
    return data


def write_dict_to_csv(filename, data):
    fieldnames = ["Monts", "Amount", "Total", "Percentage", "Sum"]  # data[0].keys()
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()  # записывает заголовок
        writer.writerows(data)


filename = "new_data.csv"
new_data = read_dict_from_csv(filename)
for row in new_data:
    row["Percentage"] = int(row["Sum"]) * 0.2
# print(new_data)
filename = "new_data_2.csv"
write_dict_to_csv(filename, new_data)