# Aggregation = Represents a relationship where one object (the whole)
#               Contains references to one or more independent objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} {book.auther}"for book in self.books]
class Book:

    def __init__(self, title, auther):
        self.title = title
        self.auther = auther


def main():

    library = Library("New York Public Library")
    book1 = Book("Herry Potter...", "J.K. Rowling")
    book2 = Book("The havit", "J. R. R. Tolkein")
    book3 = Book("The Color of Magic", "Terry Pratchet")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print(library.name)
    for book in library.list_books():
        print(book)

if __name__ == "__main__":
    main()