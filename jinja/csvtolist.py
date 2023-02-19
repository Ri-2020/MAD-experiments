import csv

def getDataFromFile(fileName):
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        rows = []
        for row in csv_reader:
            dict_row = {}
            for i in range(len(headers)):
                dict_row[headers[i]] = row[i]
            rows.append(dict_row)
    return rows

filename = "data.csv"
data = getDataFromFile(filename)
