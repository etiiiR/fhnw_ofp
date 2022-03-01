# 1 Funktion
## Anzahl Gerade mit Reduce und Filter programmieren

def anzahl_gerade(lst: list) -> int:
    return len(list(filter(lambda x: x % 2 == 0, lst)))


print(anzahl_gerade([4, 3, 6, 32, 2, 1, 23, 4]))


def anzahl_gerade2(lst: list) -> int:
    return sum([1 for x in lst if x % 2 == 0])


print(anzahl_gerade2([4, 3, 6, 32, 2, 1, 23, 4]))

from functools import reduce


def anzahl_gerade3(lst: list) -> int:
    return reduce(lambda a, b: a + 1, filter(lambda x: x % 2 == 0, lst), 0)


print(anzahl_gerade3([4, 3, 6, 32, 2, 1, 23, 4]))

def summe(x):
    def f(a,b):
        return x + a + b
    return f

foo = summe(2)
print(foo(4,5))



# 2 Funktion
from typing import Callable


def foo(x: int, y: int, z: int) -> int:
    return x + y + z
def curry(foo: Callable, k: int) -> Callable:
    return lambda *args: foo(k, *args)
bar = curry(foo, 5)
print(bar(2, 4))


def summe(x):
    def f(a,b):
        return x + a + b
    return f

foo = summe(2)
print(foo(4,5))






# 3 Nur Reduce Funktion benutzen
def mein_filter(lst: list, k: int) -> list:
    return list(filter(lambda x: x > k, lst))


print(mein_filter([1, 3, 2, 4, 5], 3))


def mein_filter2(xs: list, k: int) -> list:
    return [x for x in xs if x > k]


print(mein_filter2([1, 3, 2, 4, 5], 3))



