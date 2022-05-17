class Mob():
    def __init__(self, name, height, health, color):
        self.name = name
        self.height = height
        self.health = health
        self.color = color

    def killed(self):
        print(self.name, "was killed.")

class Creeper(Mob):
    def __init__(self, name, height, health, color, friendly, drops):
        Mob.__init__(self, name, height, health, color)
        self.friendly = friendly
        self.drops = drops

    def kill(self, mob):
        if mob == self:
            print("Not possible!")
            return
        print(self.name, "killed", mob.name)
        mob.killed()

    def killed(self):
        print(self.name, "dropped:", self.drops)

class Human(Mob):
    def __init__(self, name, height, health, color, starvation_level, items):
        Mob.__init__(self, name, height, health, color)
        self.starvation_level = starvation_level
        self.items = items

    def kill(self, mob):
        if mob == None:
            print("Not possible!")
            return
        print(self.name, "killed", mob.name)
        mob.killed()

    def killed(self):
        print(self.name, "dropped:", self.items)

class Sheep(Mob):
    def __init__(self, name, height, health, color, friendly):
        Mob.__init__(self, name, height, health, color)
        self.friendly = friendly

class Healer(Human):
    def __init__(self, name, height, health, color, starvation_level, items, talisman):
        Human.__init__(self, name, height, health, color, starvation_level, items)
        self.talisman = talisman

    def heal(self, mob):
        mob.health += 1
        if self.talisman <= 0:
            print(self.name, "can not heal!")
            return
        self.talisman -= 1
        print(self.name, "healed", mob.name)
        print(mob.name, "now has", mob.health, "health")

    def revive(self, mob):
        print(mob.name, "has been revived by", self.name)

gabu = Human("Gabu", 200, 10, "brown", 10, ["Diamond_Sword", "Sandwich", "64 Netheorite"])
lukas = Creeper("Luuzemp14", 160, 5, "green", False, "2 Gunpowders")
ben = Sheep("Ben", 50000, 20, "pink", True)
julia = Healer("Julia", 10000000, 40000000, "pink", 999, ["Healed Stone"], 0)


gabu.kill(lukas)
lukas.kill(gabu)
gabu.kill(gabu)
lukas.kill(lukas)

gabu.kill(ben)
julia.heal(gabu)

gabu.kill(None)

# Wilde shit