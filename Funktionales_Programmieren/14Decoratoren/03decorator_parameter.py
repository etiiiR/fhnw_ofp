def add_two_nums(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(add_two_nums(10,20))

def decorator(func):
    def wrapper(*args):
        return func(*args * 2)
    return wrapper

deco_func = decorator(add_two_nums)
print(deco_func(10,20))


def decorator2(func):
    def wrapper(*args):
        return func(*args * 3)
    return wrapper

deco_func2 = decorator2(deco_func)
print(deco_func2(10,20))