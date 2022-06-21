from typing import Callable

def quadratic_function(a: int,b:int,c:int) -> Callable:
    print(f"{a}* x**2 + {b}*x + {c}")
    return lambda x: a*x**2 + b*x + c

test1 = quadratic_function(1,1,1)
print(test1(10))

test2 = quadratic_function(0,10,0)
print(test2(10))



