class Menge():
    def __init__(self, liste_mit_zahlen: list):
        self.liste_mit_zahlen = liste_mit_zahlen

    MENGE_LISTE = []

    def check_menge(self):
        for x in self.liste_mit_zahlen:
            if x not in Menge.MENGE_LISTE:
                Menge.MENGE_LISTE.append(x)

liste = [1,2,4,1,3,2,5,2,4,2,4,5,2,2,4,2,1,43,4]

m1 = Menge(liste)
print(m1.liste_mit_zahlen)
m1.check_menge()
print(m1.MENGE_LISTE)


class Set():
    def __init__(self, liste: list):
        Menge_Liste = []
        for x in liste:
            if x not in Menge_Liste:
                Menge_Liste.append(x)
        self.liste = Menge_Liste
                    
liste = [1,1,2,2,3,4]
Set(liste)
