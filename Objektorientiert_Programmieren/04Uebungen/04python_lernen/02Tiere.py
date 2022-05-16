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


class Katze(Tier):
    def __init__(self, farbe, alter, rufname):
        Tier.__init__(self, farbe, alter, rufname)

katze1 = Katze("orange", 20, "min")

class Hund(Tier):
    def __init__(self, farbe, alter, rufname):
        Tier.__init__(self, farbe, alter, rufname)

hund1 = Hund("Braun", 10, "max")

hund1.schlafen(10)
print(hund1.schlafzeit)
hund1.reden(10)