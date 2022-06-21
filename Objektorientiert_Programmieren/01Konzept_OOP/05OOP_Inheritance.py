# Eine Klasse Person wird erstellt
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

p1 = Person("Ben", "Tran")
p1.printname()

# Eine Klasse Student erstellen, der die Eigenschaften und Methoden von Klasse Person beinhaltet
# Die Klasse Student erbt die Eigenschaften von Klasse Person.
class Student(Person):
    def __init__(self, firstname, lastname, startyear):
        Person.__init__(self, firstname, lastname)
        self.startyear = startyear

    def welcome(self):
        print(self.firstname, self.lastname, "started FHNW at", self.startyear)

s1 = Student("Ben", "Tran", 2019)
s1.welcome()



class Fahrzeug():
    def __init__(self, marke, farbe, x_position):
        self.marke = marke
        self.farbe = farbe
        self.x_position = x_position

    def fahren(self, strecke):
        self.x_position += strecke

class Velo(Fahrzeug):
    def __init__(self, marke, farbe, x_position, max_geschwindigkeit):
        Fahrzeug.__init__(self, marke, farbe, x_position)
        self.max_geschwindigkeit = max_geschwindigkeit

velo1 = Velo("Cube", "grau", 0, 25)
print(velo1.marke)

velo1.fahren(100)
print(velo1.x_position)


class Flugzeug(Fahrzeug):
    def __init__(self, marke, farbe, x_position, y_position, max_speed):
        Fahrzeug.__init__(self, marke, farbe, x_position)
        self.y_position = y_position
        self.max_speed = max_speed

    def fahren(self, x_change, y_change):
        self.x_position += x_change
        self.y_position += y_change


airbus900 = Flugzeug("Airbus", "weiss", 0, 0, 500)
airbus900.fahren(10, -10)
print(airbus900.x_position, airbus900.y_position)