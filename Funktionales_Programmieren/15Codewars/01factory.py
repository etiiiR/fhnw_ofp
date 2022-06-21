array = [1,2,3]

def factory(y:int):
    def mal_list(liste):
        return list(map(lambda x: x * y, liste))
    return mal_list

factor = factory(5)
print(factor)
print(type(factor))

print(factor(array))
