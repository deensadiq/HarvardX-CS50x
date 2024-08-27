books = []

for i in range(3):
    book = dict()
    book["title"] = input("Enter a title: ")
    book["author"] = input("Enter an author: ")
    books.append(book)
    

for book in books:
    print(book["author"])
    print(book["title"])