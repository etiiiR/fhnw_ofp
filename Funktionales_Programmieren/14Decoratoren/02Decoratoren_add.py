def add_two(a, b):
    return a + b

def double_decorator(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)
    return wrapper

add_two_deco = double_decorator(add_two)
print(add_two_deco(10,20))

def add_multiply(a, b):
    return a + b + a * b

def add_1_multiply_3(func):
    def wrapper(a, b):
        return func(a + (1 * 3), b + (1 * 3))
    return wrapper

add_multiply_decorator = add_1_multiply_3(add_multiply)
print(add_multiply_decorator(2,3))

print(add_multiply(5, 6))