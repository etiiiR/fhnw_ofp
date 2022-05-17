class Katze():
    def __init__(self, farbe, alter, name, anzahl_beine):
        self.farbe = farbe
        self.alter = alter
        self.name = name
        self.anzahl_beine = anzahl_beine

    def miauen(self, anzahl):
        print("Miau" * anzahl)


objekt1 = Katze("Orange", 10, "Carlo", 4)
objekt2 = Katze("Braun", 2, "Luu", 4)

objekt1.miauen(10)
print(objekt1.name)