import csv
import os

FILE = "library.csv"

def init():
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='') as f:
            csv.writer(f).writerow(["ISBN", "Title", "Author", "Genre"])

def save_book_to_file(isbn, title, author, genre):
    init()
    with open(FILE, 'a', newline='') as f:
        csv.writer(f).writerow([isbn, title, author, genre])
    print("Saved successfully.")

def read_all_books():
    init()
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return list(csv.reader(f))[1:] # Returns list skipping header
    return []