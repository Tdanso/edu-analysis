
import csv


list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
print(len(list_data))


# state_data = [row for row in list_data if row["STATE"] == "NEW_YORK"]
# # state_data = [row for row in list_data if ]
# print(state_data)
# print(len(state_data))
# state_data = [row for row in state_data if row["AVG_MATH_4_SCORE"] != '']
# print(state_data) 
# print(len(state_data))


def filter(state , column):
    state_data = [row for row in list_data if row["STATE"] == state]
    score_data = [row[column] for row in state_data]
    return score_data
result = filter("NEW_YORK", "AVG_READING_4_SCORE")

years = [row["YEAR"] for row in list_data if row["STATE"] == "NEW_YORK" and row["AVG_READING_4_SCORE"] != ""]
print(years)



years = []
years = [(row["YEAR"]) for row in state_data]
for row in state_data:
    years.append(row["YEAR"])
    years.sort()
    print(years)

# years = [(row["YEAR"]) for row in state_data]
# print(years)


def percent_change(data, year1, year2, column):
    """
    
    
    
    
    
    """
    old = 0
    new = 0
    for row in data:
        if row["YEAR"] == year1:
            old = row[column]
        if row["YEAR"] == year2:
            new = row[column]

    percent_change = (float(old) - float(new))/float(old) * 100
    return percent_change


print(percent_change(state_data, "2009", "2011", "AVG_MATH_4_SCORE"))

# applying percent change
# perc_change = []
for i in range(len(years)-1):
    # if i + 1 >= len(years):
    #     break
    year1 = years[i]
    year2 = years[i + 1]
    change = percent_change(state_data, year1, year2, "AVG_MATH_8_SCORE")
    print(f"NY percentage change from {year1}-{year2} is {round(change,2)}")

perc_change = [
    {"range": "2000-2003", "percent change": -3.21},
    {"range": "2003-2005", "percent change": -4.89},
    {"range": "2005-2007", "percent change": -2.1}

]















