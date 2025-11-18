class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__is_available = True  


    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author


    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"You have borrowed '{self.__title}'.")
        else:
            print(f"Sorry, '{self.__title}' is not available.")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"You have returned '{self.__title}'.")
        else:
            print(f"'{self.__title}' was not borrowed.")

    def is_available(self):
        return self.__is_available


book1 = Book("1984", "George Orwell", 328)


print(book1.title)
print(book1.author)

book1.borrow()
print(book1.is_available())
book1.return_book()
print(book1.is_available())

