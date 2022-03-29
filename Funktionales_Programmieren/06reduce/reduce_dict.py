from functools import reduce

def mein_filter(func, liste):
    return reduce(lambda a, b: a + [b] if func(b) else a, liste, dict())

liste_dict = [{"Key":10},{"Key":20},{"Key":30}]

print(mein_filter(lambda x: [x] <= 20, liste_dict))


for key, values in liste_dict.

