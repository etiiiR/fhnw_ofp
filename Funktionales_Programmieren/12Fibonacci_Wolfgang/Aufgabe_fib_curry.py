from typing import Callable

def fibonacci_rec(n: int) -> int:

    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def curry_mean() -> Callable[[],int]:
    def mean(liste: list) -> int:
        return sum(liste) / len(liste)
    return mean

mean = curry_mean()
mean_5 = mean([fibonacci_rec(i) for i in range(1, 6)]) # [1, 1, 2, 3, 5]
print(mean_5) # 12/5