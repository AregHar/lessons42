"""
keywords: Code/implementation reuse, identity, single-inheritance
"""

from lesson_1_oop._1_book_encapsulation import Book


class Ebook(Book):
    MAX_SIZE = float('inf')

    def __init__(self, title: str, size: int):
        title += ' (digital edition)'
        super(Ebook, self).__init__(title, size)


class AudioBook(Ebook):
    def read_page(self) -> None:
        print("reading {} on page {} aloud!".format(self.title, self.current_page))


# client code
if __name__ == "__main__":
    from lesson_1_oop._1_book_encapsulation import Book
    from lesson_1_oop._2_book_inheritance import Ebook, AudioBook

    book = Ebook("python tuts", 20)

    book.read_page()
    book.read_through()

    print(isinstance(book, Book))
    print(isinstance(book, Ebook))
    print(isinstance(book, AudioBook))

    book = AudioBook("python tuts", 20)

    book.read_page()
    book.read_through()

    # print(isinstance(book, Book))
    # print(isinstance(book, Ebook))
    # print(isinstance(book, AudioBook))
    #
    # print(issubclass(AudioBook, Ebook))
    # print(issubclass(AudioBook, Book))
    # print(issubclass(Book, AudioBook))
    #
    # # TODO internal
    # print(Book.__mro__)
