import time

# from functools import lru_cache


class Cache:
    _cache = {}

    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        if args not in self._cache:
            print("no cache, calling the real function")
            self._cache[args] = self._func(*args)
        return self._cache[args]


@Cache  # decoration via init
def heavy_calculation(a, b):
    time.sleep(2)
    return a + b


# heavy_calculation = Cache(heavy_calculation)

value = heavy_calculation(1, 2)
print(value)

value = heavy_calculation(1, 2)
print(value)
