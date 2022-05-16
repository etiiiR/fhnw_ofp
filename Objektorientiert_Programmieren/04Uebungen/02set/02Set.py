class Set():
    def __init__(self, list_of_num: list):
        Menge_Liste = []
        for x in list_of_num:
            if x not in Menge_Liste:
                Menge_Liste.append(x)
        self.menge_liste = Menge_Liste

    def __str__(self):
        result = self.menge_liste
        return result

lst_with_nums = [1, 1, 2, 2, 3, 4]
print(Set(lst_with_nums))

