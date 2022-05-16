class Bruch():
    def __init__(self, zaehler:int , nenner:int):
        self.zaehler = zaehler
        self.nenner = nenner

    def bruch(self, z:int, n:int):
        return z / n

    def erweitern(self, k:int):
        return (self.zaehler / self.nenner) * k

    def kuerzen(self, k:int):
        return (self.zaehler / self.nenner) / k

b = Bruch(10,5)
b.kuerzen(2)
b.erweitern(2)
print(b.erweitern(3))