class Person:
    num_of_person = 0

    def __init__(self, name):
        self.name = name
        Person.num_of_person += 1

    @classmethod
    def number_of_people(cls):
        return cls.num_of_person

p1 = Person("Ben")
print(p1.number_of_people(), Person.num_of_person)
p2 = Person("NochmalsBen")
print(p2.number_of_people(), Person.num_of_person)

# Klassenattribute verwendet man bei Werten die sich nicht aendern.
# Bsp: Startpunkt 0
# Gravitation 9.81
# etc...
