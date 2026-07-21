class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def show_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)

    def get_number_of_books(self):
        print("Total books:", self.no_of_books)

    def check_books(self):
        if self.no_of_books == len(self.books):
            print("Number of books is equal to the length of books list.")
        else:
            print("Something is wrong. Number of books does not match.")


library = Library()

library.add_book("Python Programming")
library.add_book("C++ Programming")
library.add_book("Data Structures")

library.show_books()
library.get_number_of_books()
library.check_books()