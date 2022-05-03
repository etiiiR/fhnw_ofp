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
