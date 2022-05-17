class Tier():
    def __init__(self, farbe, alter, rufname):
        self.farbe = farbe
        self.alter = alter
        self.rufname = rufname
        self.schlafzeit = 0

    def schlafen(self, stunden):
        self.schlafzeit += stunden

    def reden(self, anzahl=1):
        print(self.rufname * anzahl)

    def append(self, anzahl):
        pass


class Katze(Tier):
    pass

katze1 = Katze("orange", 20, "mini")

class Hund(Tier):
    pass

hund1 = Hund("Braun", 10, "maxi")

hund1.schlafen(10)
print(hund1.schlafzeit)
hund1.reden(10)

katze1.reden(3)

print(katze1.rufname)


x = [1,2,3,5]

print(type(x))


class list():
    def append(self):
        pass

    def remove(self):





print(katze1.__dict__)
