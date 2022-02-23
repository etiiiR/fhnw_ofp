from typing import Callable

def mal(x: int) -> Callable[[int], int]:
    def mal_x(y: int) -> int:
        return x * y
    return mal_x

def multipliziere_liste_funktional(lst: list, factor: int) -> list:
    mal_factor = mal(factor)
    return list(map(lst, mal_factor))

print(multipliziere_liste_funktional([10,20],2))