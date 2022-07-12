


def decorator(func):
    dict = {}

    def wrapper(*args, **kwargs):
        result_stored = dict.get(*args)
        if result_stored is not None:
            return result_stored
        res = func(*args, *kwargs)
        dict[args] = res
        return res

    return wrapper

@ decorator
def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(100))