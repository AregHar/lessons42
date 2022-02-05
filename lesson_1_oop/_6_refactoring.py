"""
keywords: Data hiding, public, private, data_mingling, coupling, versioning, backward compatibility,
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
        self._current_page = 1  # edited

    # read only
    @property  # edited
    def current_page(self) -> int:
        return self._current_page

    # implementation detail
    def _generate_page(
        self,
    ):  # edited
        return "reading {} on page {}".format(self.title, self._current_page)

    def read_page(self) -> None:
        print(self._generate_page())  # edited

    def turn_the_page(self, n: int = 1) -> None:
        new_page = self._current_page + n

        # check boundary conditions
        if new_page < 1 or new_page > self.size:
            raise ValueError("Cannot turn the page")

        self._current_page = new_page  # edited

    def read_through(self) -> None:
        try:
            while True:
                self.turn_the_page()
                self.read_page()
        except ValueError:
            pass


# client code
if __name__ == "__main__":
    from lesson_1_oop._6_refactoring import Book

    book = Book("tuts", 5)
    book.read_through()

    book._current_page  # change the private field so that the client code to crashes
