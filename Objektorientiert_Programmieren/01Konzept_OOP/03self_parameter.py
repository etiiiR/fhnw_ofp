# Warum der Self Parameter wichtig ist
# wir koennen aus der Classe mehrere Objekte erstellen
# Alle Objekte referenzieren auf einen bestimmten Speicherplatz
# Dort befinden sich alle Attributwerte des jeweiligen Objektes
# Aendern wir nun ein Attribut, muss man wissen auf welchen konkreten
# Objekt die Bearbeitung nun stattfinden darf. (Man kann ja mehrere Objekte
# erstellen)
# Durch das self wird beim Aufrufen der init methode die Referenz
# auf das Objekt mituebergeben

# Was ist eine Referenz

class Car:
    def __init__(self):
        self.car_brand = None
        self.car_color = None
        self.car_power = None

car1 = Car() # Car Objekt 1
car1.car_brand = "VW"

print(car1) # Gibt mir die Adresse des Objektes.
# Car1 beinhaltet eine Referenz wo die Daten gespeichert sind.

car3 = car1 # car1 beinhaltet nur die Referenz, wo die Daten gespeichert sind.
print(car3)

# die Adresse von car3 ist gleich wie die von car1!

print(car1.car_brand, car3.car_brand)