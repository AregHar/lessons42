"""
keywords: Protocols, syntactic sugar, Pythonic/idiomatic code
"""


class Number:
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return "This is the number {}".format(self.value)

    def __repr__(self):
        return "Number({})".format(self.value)

    def __add__(self, other) -> "Number":  # or int. discuss mathematical closure!!
        return Number(self.value + other.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __bool__(self) -> bool:
        return self.value != 0


n = Number(20)
m = Number(22)

print(n)
print(repr(n))

# operator overloading via type-based polymorphism
print(n + m)

print(n == n)
print(n == m)

# truthy/falsy values
if Number(0):
    print('will not run')

if Number(1):
    print('will run')


class Queue:
    def __init__(self, values):
        self._list = []
        for value in values:
            self.enqueue(value)

    def enqueue(self, value) -> None:
        self._list.append(value)

    def dequeue(self):
        return self._list.pop(0)

    def __len__(self):
        return len(self._list)

    def __iter__(self):  # iterable protocol
        # try:
        #     while True:
        #         yield self.dequeue()
        # except IndexError:
        #     return

        return self

    # this could be a separate class, iterator protocol
    def __next__(self):
        if not len(self):
            raise StopIteration
        return self.dequeue()


q = Queue([1, 2])
print(len(q))

q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(len(q))

print(list(Queue([1, 2])))


# subscription protocol
class Sentence:
    def __init__(self, text: str):
        self._words = text.split()

    def __str__(self):
        return ' '.join(self._words)

    def __iter__(self):
        return iter(self._words)

    def __getitem__(self, item):
        return self._words[item]

    def __setitem__(self, key, value):
        self._words[key] = value

    def __delitem__(self, key):
        del self._words[key]

    def __len__(self):
        return len(self._words)

    def is_question(self) -> bool:
        return self._words[-1].endswith('?')


s = Sentence("This is getting fun!")
print(s)

for word in s:
    print(word)

print(s[3])
s[3] = 'hot'
del s[2]
print(s)

print(s[:2])
del s[1:2]
print(s)


# dot notation protocol
class SmartMock:
    def __init__(self):
        self._calls = []

    def _register_call(self, call):
        self._calls.append(call)

    def history(self):
        return self._calls

    def __call__(self, *args, **kwargs):
        self._register_call(f'called with args {args} & kwargs {kwargs}')

    def __getattr__(self, item):
        self._register_call(f'accessed attribute {item}')
        return self

    # TODO homework
    # __setattr__
    # __delattr__


from lessons.polymorphism import book_reader

spy = SmartMock()
book_reader(spy)

print(spy.history())
