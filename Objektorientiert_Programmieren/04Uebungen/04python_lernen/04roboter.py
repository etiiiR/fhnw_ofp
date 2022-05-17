import random
class Robot():
    def __init__(self, name):
        self.name = name
        self.health = random.randint(0, 20)

    def say_hi(self):
        print("Hi my name is ", self.name)

    def needs_a_doctor(self):
        if self.health < 3:
            return True
        else:
            return False


class healbot(Robot):

    def say_hi(self):
        print("Hi, ich heisse", self.name ,"und es wird alles wieder gut!")

    def heal(self, robo):
        robo.health += robo.health + 1
        print(robo.name, "wurde von", self.name, "geheilt")

doc = healbot("Frankenstein")
patient1 = Robot("Ben")

doc.say_hi()
doc.heal(patient1)
