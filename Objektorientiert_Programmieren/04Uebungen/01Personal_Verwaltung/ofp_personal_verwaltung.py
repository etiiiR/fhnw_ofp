class Person():
    def __init__(self, name, anschrift):
        self.name = name
        self.anschrift = anschrift


class Mitarbeiter(Person):
    def __init__(self, name, anschrift, gehalt, eintrittsdatum):
        Person.__init__(self, name, anschrift)
        self.gehalt = gehalt
        self.eintrittsdatum = eintrittsdatum


class Praktikant(Person):
    def __init__(self, name, anschrift, eintrittsdatum, laufzeit):
        Person.__init__(self, name, anschrift)
        self.eintrittsdatum = eintrittsdatum
        self.laufzeit = laufzeit


class Manager(Mitarbeiter):
    def __init__(self, name, anschrift, gehalt, eintrittsdatum, praemie):
        Mitarbeiter.__init__(self, name, anschrift, gehalt, eintrittsdatum)
        self.praemie = praemie
        self.gehalt = self.gehalt + self.praemie


mgr1 = Manager("Ben", "Herr", 100000, 2020, 3000)
print(mgr1.gehalt)

prak1 = Praktikant("Ben", "Herr", 2020, 2022)
print(prak1.laufzeit)

mit1 = Mitarbeiter("Ben", "Herr", 100000, 2020)
print(mit1.gehalt)