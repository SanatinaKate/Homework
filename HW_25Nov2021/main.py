from csv import DictReader
from json import dump, load

books = []
with open("/VV/QAPython/Homework/HW_25Nov2021/files/books.csv", "r") as f:
    reader = DictReader(f)
    for row in reader:
        book = {}
        for key in ("Title", "Author", "Pages", "Genre"):
            book[key.lower()] = row[key]
        books.append(book)
books_len = len(books)

users = []
with open("/VV/QAPython/Homework/HW_25Nov2021/files/users.json", "r") as f:
    users_load = load(f)
users_len = len(users_load)

number_of_books = books_len // users_len
rest_of_books = books_len % users_len
i = 0
for row in users_load:
    user = {}
    for key in ("name", "gender", "address", "age"):
        user[key] = row[key]
    j = i + number_of_books
    if row["index"] < rest_of_books:
        j = j + 1
    user["books"] = books[i:j]
    i = j
    users.append(user)

with open("/VV/QAPython/Homework/HW_25Nov2021/files/result.json", "w") as f:
    dump(users, f, indent=4)
