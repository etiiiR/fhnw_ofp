class Fahrzeug():
    def __init__(self, farbe, anzahl_rad, anzahl_platz):
        self.farbe = farbe
        self.anzahl_rad = anzahl_rad
        self.anzahl_platz = anzahl_platz

class Velo(Fahrzeug):
    pass

Velo1 = Velo("Orange", 2, 2)
    