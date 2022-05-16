fib_dict = {0:0, 1:1}
def fibonacci_rec_cnt(n: int):
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fibonacci_rec_cnt(n - 1) + fibonacci_rec_cnt(n - 2)
        return fib_dict[n]

print(fibonacci_rec_cnt(8), fib_dict)