from functools import reduce

def mein_filter(func, liste):
    return reduce(lambda a, b: a + [b] if func(b) else a, liste, [])

print(mein_filter(lambda x: x > 4, [1,2,3,4,5,6,7,8]))


