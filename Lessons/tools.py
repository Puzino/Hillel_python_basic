import csv


def read_dict_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
    return data


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
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


def write_to_csv(filename, data, delimiter=","):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


print(__name__)
if __name__ == "__main__":
    filename = "new_data_2.csv"
    new_data = read_from_csv(filename)
    print(new_data)