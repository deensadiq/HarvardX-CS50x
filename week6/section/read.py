import csv

books = []

with open("books2.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)