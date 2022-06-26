class Kunde():
    def __init__(self, vorname, nachname, saldo, inventar):
        self.vorname, self.nachname = vorname, nachname
        self._saldo = saldo
        self.inventar = inventar

    def check_saldo(self):
        print(self.vorname + " " + self.nachname + "hat ein Saldo von: " + self._saldo)

    def request_Pommes(self):
        print("Will gerne Pommes, bitte")
        Mitarbeiter.mayoAsk(self)

    def getpommes(self, objekt):
        self.inventar.append(objekt)

    def eatpommes(self):
        self.inventar = []

class Mitarbeiter():
    def __init__(self, vorname, nachname, saldo, inventar):
        self.vorname, self.nachname = vorname, nachname
        self._saldo = saldo
        self.inventar = inventar

    def mayoAsk(self):
        question = input("Willst du Mayo? (Y/N) ")
        if question == "Y":
            pommes = Pommes(100)
            Kunde.getpommes(self, pommes)

        elif question == "N":
            print("Sorry, Pommes ohne Mayo laeuft nicht!")

class Pommes():
    def __init__(self, menge):
        self.menge = menge

# Objekte erstellen
kunde1 = Kunde("Jun", "Jay", 200, [])
mitarbeiter1 = Mitarbeiter("Han", "Hoooo", 5900, [])

# Kunde will Pommmes
kunde1.request_Pommes()

# Inventar von Kunden ausgeben
print(kunde1.inventar)

# Kunde isst Pommes
kunde1.eatpommes()

# Inventar von Kunden ausgeben
print(kunde1.inventar)