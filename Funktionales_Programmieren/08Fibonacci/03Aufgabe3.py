# leeres fib_dict
def fibonacci_rec(n: int) -> int:
    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

fib_dict = {}

cnt = 0
def fibonacci_rec_func(x: int):
    global cnt
    cnt += 1
    if x in fib_dict:
        print(fib_dict[x])
    else:
        fib_dict[x] = fibonacci_rec(x)
        print(fib_dict[x])

fibonacci_rec_func(19)
print(fib_dict)


