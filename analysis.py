
import csv


list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

# state_data = [row for row in list_data if ]
print(list_data)
# print(state_data)