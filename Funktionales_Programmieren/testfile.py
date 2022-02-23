from typing import Callable


def mal(x: int) -> Callable[[int], int]:
    def mal_x(y: int) -> int:
        return x * y

    return mal_x


def multipliziere_liste_funktional(xs: list, k: int) -> list:
    mal_k = mal(k)
    print(list(map(mal_k, xs)))


multipliziere_liste_funktional([10, 20], 2)
