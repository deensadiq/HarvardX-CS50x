books = []

for i in range(3):
    book = dict()
    book['author'] = input("Enter an author: ")
    book['title'] = input("Enter book title: ")
    books.append(book)
    
# Print list of Books
for book in books:
    print(book)
    
# Print distionaru keys
for book in books:
    print(book.keys())