import csv

books = []

# Add books to shelf by reading from books.csv
with open("books.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)