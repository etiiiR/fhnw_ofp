# Methoden in Klassen

# OOP Zusammenfassung
# Mit OOP versuchen wir Komplexe Objekte der Realte Welt zu modellieren
# Attribute legen wir in der __init__ Methode fest.
# Die Klasse stellt nur den Bauplan des Objektes dar
# Von einer Klasse kan man ein oder mehrere Objekte erzeugen
# Bei Erzeugung eines Objektes, wird intern der Speicher reserviert und alle Daten die das Objekt betreffen
# werden im Speicher festgehalten (Bsp. Attribute)
# Punktoperator -> Schreibweise um ueber Referenz auf spezifische Attribute zugreifen zu koennen

# Erweiterung der Methoden mit einer Weiteren Methoden
class Car:
    def __init__(self):
        self.car_brand = None
        self.car_color = None
        self.car_power = None
        self.x_position = 5
        self.y_position = 5

    def drive(self, x, y):
        self.x_position += x
        self.y_position += y

car1 = Car()
# Ausgabe der x und y Position
print(car1.x_position, car1.y_position)

# Das Auto Fahren lassen
car1.drive(10,5)

# Ausgabe der x und y Position, nachdem Fahren
print(car1.x_position, car1.y_position)
