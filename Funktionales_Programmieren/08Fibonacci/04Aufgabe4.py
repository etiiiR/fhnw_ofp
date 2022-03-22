def fibonacci_rec(n: int) -> int:
    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_rec_cnt(n: int, cnt=0) -> tuple:
    cnt += 1
    return cnt, n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

fib_dict_2 = {}

def fibonacci_rec_func2(x: int):
    if x in fib_dict_2:
        print(fib_dict_2[x])
    else:
        fib_dict_2[x] = tuple(fibonacci_rec_cnt(x))


fibonacci_rec_func2(31)
print(fib_dict_2)