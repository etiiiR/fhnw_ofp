def add_first(a):
    def add_second(b):
        return a + b
    return add_second

def decorator(func):
    def wrapper(a):
        return func(a * 2)
    return wrapper

deco_add_first = decorator(add_first)
add_second = deco_add_first(10)
deco_add_second = decorator(add_second)
print(deco_add_second(50))

print(add_second.__closure__[0].cell_contents)
print(len(add_second.__closure__))