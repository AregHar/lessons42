"""
keywords: -
"""


from lesson_1_oop._1_book_encapsulation import Book


class Mock:
    """Foo doc-line"""
    pass


mock = Mock()


def show_internals(obj):
    for key, value in vars(obj).items():
        print(key, value)

    print()


# show_internals(mock)
# show_internals(Book("title", 42))

# show_internals(Mock)
show_internals(Book)


class Mock:
    def __new__(cls, *args, **kwargs):
        return super(Mock, cls).__new__(*args, **kwargs)

    # order of __new__, __init__, __call__