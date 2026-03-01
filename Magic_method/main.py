# Magic methods = Dunder methods (double underscore) __int__, __str__,__eq__
#                 They are autometically called by many of Python's build in operations
#                 They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, auther, num_pages):
        self.title = title
        self.auther = auther
        self.num_pages = num_pages


    # STRING represantation of an objact
    def __str__(self):
        return f"'{self.title}' by {self.auther}"

    def __eq__(self, other):
        return self.title == other.title and self.auther == other.auther

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or self.auther

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "auther":
            return self.auther
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"

def main():

    book1 = Book("The Havit", "J. R. R. Tolkien", 310)
    book2 = Book("Herry Potter and The Philosopher's Stone", "J.K Rowling", 223)
    book3 = Book("The Lion, the Witch and the wardrobe", "J.K Rowling", 172)
    book4 = Book("The Havit", "J. R. R. Tolkien", 308)

    print(book1)
    print(book1 == book4)
    print(book2 < book3)
    print(book2 > book3)
    print(book2 + book3)
    print("Rowling" in book3)
    print(book3['audio'])

if __name__ == "__main__":
    main()