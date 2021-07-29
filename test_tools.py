from tools import read_from_csv

filename = "new_data.csv"
new_data = read_from_csv(filename)
assert len(new_data[0]) == 4
print(new_data)