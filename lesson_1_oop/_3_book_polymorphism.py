"""
keywords: Interface, duck typing (structural vs nominal typing)
"""

from lesson_1_oop._1_book_encapsulation import Book


def book_reader(book: Book):
    print("let's see what book is this {}...")
    print("Hmm, {}".format(book.title))
    book.turn_the_page(1)

    book.read_page()
    book.turn_the_page()
    book.read_page()

    print("Mmm, not bad. I'm going to like python!")
    book.read_through()
    print("Finished reading book {}, phew.".format(book.title))


# client code
if __name__ == "__main__":
    from lesson_1_oop._1_book_encapsulation import Book
    from lesson_1_oop._2_book_inheritance import AudioBook, Ebook
    from lesson_1_oop._3_book_polymorphism import book_reader

    # book = Book("python tuts", 5)
    # book = Ebook("C tuts", 5)
    book = AudioBook("Java tuts", 5)

    book_reader(book)
