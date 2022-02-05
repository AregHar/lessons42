"""
keywords: Cohesion, abstraction through encapsulation, object, class, instance, type vs token
"""


class Book:  # reserved keyword -- escaped version are cls, klass, class_
    MAX_SIZE = 800  # add this piece later, when implementing the inheritance

    def __init__(self, title: str, size: int):  # ctor vs initializer
        if size < 1:
            raise ValueError("A book needs to have at least one page")
        if size > self.MAX_SIZE:  # refactor this from size > 800
            raise ValueError("A single volume cannot be bigger than 800 pages")

        # instance variables/fields
        self.title = title  # supplied by the client code

        # check size boundaries
        self.size = size
        # TODO page is linked to a single reader, book can be read by many, we need to keep the volatile state outside, need to decouple
        self.current_page = 1

    def read_page(self) -> None:
        print("reading {} on page {}".format(self.title, self.current_page))

    def turn_the_page(self, n: int = 1) -> None:
        new_page = self.current_page + n

        # check boundary conditions
        if new_page < 1 or new_page > self.size:
            raise ValueError("Cannot turn the page")

        self.current_page = new_page

    def read_through(self) -> None:
        try:
            while True:
                self.turn_the_page()
                self.read_page()
        except ValueError:
            pass


# client code
if __name__ == "__main__":
    from lesson_1_oop._1_book_encapsulation import Book

    book = Book("python tuts", 5)

    book.read_page()

    book.turn_the_page()

    book.read_page()

    book.read_through()

    print(book)

    # abuse
    book.current_page = 42
    book.read_page()  # could raise error
