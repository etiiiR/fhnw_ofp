import functools
import timeit
from typing import Callable
import numpy as np


# Helpers

def timeFunc(func: Callable):
    def wrap(*args, **kwargs):
        vals = []
        for _ in range(50):
            start = timeit.timeit()
            func(*args, **kwargs)
            end = timeit.timeit()
            vals.append(end - start)
        print(func.__name__, np.average(vals))
        return func(*args, **kwargs)

    return wrap


def fibonacci_rec_default(n: int) -> int:
    return n if n <= 1 else fibonacci_rec_default(n - 1) + fibonacci_rec_default(n - 2)


def fibonacci_rec_aufgabe_2(n: int, c=[]) -> int:
    c.append(0)
    return n if n <= 1 else fibonacci_rec_aufgabe_2(n - 1, c) + fibonacci_rec_aufgabe_2(n - 2, c)


def aufgabe_2():
    arr = []
    res = fibonacci_rec_aufgabe_2(10, arr)
    print(res, len(arr))


def fibonacci_rec_aufgabe_3(n: int, dct={}) -> int:
    if dct.get(n) is not None:
        return dct[n]

    res = n if n <= 1 else fibonacci_rec_aufgabe_3(n - 1, dct) + fibonacci_rec_aufgabe_3(n - 2, dct)
    dct[n] = res

    return res


def aufgabe_3():
    print(fibonacci_rec_aufgabe_3(10))


@functools.cache
def fibonacci_rec_aufgabe_4(n: int) -> int:
    return n if n <= 1 else fibonacci_rec_aufgabe_4(n - 1) + fibonacci_rec_aufgabe_4(n - 2)


def aufgabe_5():
    [timeFunc(func)(34) for func in [fibonacci_rec_aufgabe_2, fibonacci_rec_aufgabe_3, fibonacci_rec_aufgabe_4]]















def my_cache(func: Callable):
    dct = {}

    def wrap(*args, **kwargs):
        storedResult = dct.get(hash(*args))
        if storedResult is not None:
            return storedResult
        res = func(*args, **kwargs)
        dct[hash(*args)] = res
        return res

    return wrap



@my_cache
def fibonacci_rec_aufgabe_6(n: int) -> int:
    return n if n <= 1 else fibonacci_rec_aufgabe_6(n - 1) + fibonacci_rec_aufgabe_6(n - 2)


def fibonacci_rec_aufgabe_6_no_cache(n: int) -> int:
    return n if n <= 1 else fibonacci_rec_aufgabe_6_no_cache(n - 1) + fibonacci_rec_aufgabe_6_no_cache(n - 2)


@timeFunc
def exec_fib_cache(n):
    fibonacci_rec_aufgabe_6(n)


@timeFunc
def exec_fib_no_cache(n):
    fibonacci_rec_aufgabe_6_no_cache(n)











def aufgabe_6():
    print(fibonacci_rec_aufgabe_6(10))


@functools.cache
def fibonacci_rec_aufgabe_7(n: int) -> int:
    return n if n <= 1 else fibonacci_rec_aufgabe_7(n - 1) + fibonacci_rec_aufgabe_7(n - 2)


def fibonacci_generator(n=-1):
    cnt = -1
    while cnt < n or n == -1:
        cnt += 1
        yield fibonacci_rec_aufgabe_7(cnt)


def fib_sum_1(n: int) -> int:
    sum_ = 0
    for i, f in enumerate(fibonacci_generator()):
        sum_ += f
        if i == n:
            break
    return sum_


def fib_sum_2(n: int) -> int:
    return sum(f for f in fibonacci_generator(n))


def aufgabe_7():
    print(fib_sum_1(1000))
    print(fib_sum_2(1000))


def squares_of_even_fibonacci(n):
    return sum((f ** 2 for f in fibonacci_generator(n) if f % 2 == 0))


def aufgabe_8():
    print(squares_of_even_fibonacci(6))


def fibonacci_aufgabe_9(l: int) -> int:
    cur, prev, n = 1, 0, 0
    for _ in range(l):
        cur, prev, n = cur + prev, cur, n + 1
    return cur


def aufgabe_9():
    print(fibonacci_aufgabe_9(4))


if __name__ == '__main__':
    exec_fib_no_cache(40)
    exec_fib_cache(40)
