class Student():
    def __init__(self, vorname, nachname, noten, alter):
        self.vorname = vorname
        self.nachname = nachname
        self.noten = noten
        self.alter = alter

    def get_noten(self):
        return self.noten

class Module():
    def __init__(self, lehrer, modul, max_anzahl):
        self.lehrer = lehrer
        self.modul = modul
        self.max_anzahl = max_anzahl
        self.studenten = []

    def add_student(self, student):
        if len(self.studenten) < self.max_anzahl:
            self.studenten.append(student)

    def get_average_noten(self):
        value = 0
        for stud in self.studenten:
            value += stud.get_noten()
        return value / len(self.studenten)

s1 = Student("Bla", "Kub", 100, 20)
s2 = Student("aos", "Sj", 50, 30)
s3 = Student("Aiosu", "io132", 75, 20)

daw = Module("Scredic", "daw", 2)
daw.add_student(s1)
print(daw.studenten[0].vorname)
daw.add_student(s3)
print(daw.studenten[1].vorname)

print(daw.get_average_noten())