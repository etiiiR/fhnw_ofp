# Bei OOP baut man sich ein Datentyp indem man sich eine Klasse definiert
# Eine Klasse ist ein Bauplan

class Car:
    # Eine __init__ Methode erstellen
    # Innerhalb einer Klasse redet man von Methoden und nicht von Funktionen
    def __init__(self):
        # Hier werden die Eigenschaften/Attribute zu Car definiert
        # Alle Methoden haben den Self Parameter
        self.car_brand = None
        self.car_horse_power = None
        self.car_color = None


# Objekt erzeugen und in car1 speichern
car1 = Car()
print(car1.car_brand) # Zugreifen auf das Attribute car_barnd

# Einem Attribut einen Wert zuweisen
car1.car_brand = "VW"
print(car1.car_brand)

car1.car_color = "Black"
car1.car_horse_power = "125 PS"

# Man kann nun beliebig viele Objekte erzeugen
car2 = Car()
car3 = Car()

# Jedes Objekt hat die gleichen Attribute, jedoch unterschiedliche Werte