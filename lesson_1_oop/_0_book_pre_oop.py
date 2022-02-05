# create a book
book_ = {
    "title": "python tuts",
    "size": 20,
    "current_page": 1,
}


# create a book factory, add validations
def create_book(title: str, size: int) -> dict:
    if size < 1:
        raise ValueError("A book needs to have at least one page")
    if size > 800:
        raise ValueError("A single volume cannot be bigger than 800 pages")

    return {"title": title, "size": size, "current_page": 1}


def read_page(book: dict) -> None:
    print("reading {} on page {}".format(book["title"], book["current_page"]))


def turn_the_page(book: dict, n: int = 1) -> None:
    new_page = book["current_page"] + n

    # check boundary conditions
    if new_page < 1 or new_page > book["size"]:
        raise ValueError("Cannot turn the page")

    book["current_page"] = new_page


def read_through(book: dict) -> None:
    try:
        while True:
            turn_the_page(book)
            read_page(book)
    except ValueError:
        pass


# ----- client code -----
if __name__ == "__main__":
    from lesson_1_oop.book_dict import (
        create_book,
        read_page,
        turn_the_page,
        read_through,
    )

    book = create_book("python tuts", 5)
    # book = create_book("python tuts", 900)

    read_page(book)

    turn_the_page(book)

    read_page(book)

    read_through(book)

    print(book)  # nonsensical at this point

    # abuse
    book["current_page"] = 42
    read_page(book)  # could raise error
