from functools import reduce


liste = [1,2,3,4]


a = lambda x1, x2: x1 - x2
b = lambda x1, x2: x1 + x2

def summieren(lst: list) -> int:
    return reduce(b, lst, 1)

print(summieren(liste))



def sum_summieren(lst: list):
    return sum(lst)

