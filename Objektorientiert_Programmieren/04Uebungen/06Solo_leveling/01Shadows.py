import random

class Hero():
    def __init__(self, name, guild, rank, level, shadows):
        self.name, self.guild = name, guild
        self.rank = rank
        self.level = level
        self.shadows = shadows

    def monster_disintegrated(self, monster):
        print(monster.name, "disintegrated")

    def shadow_extraction(self, monster):
        chance = random.randint(1,3)
        print(chance)
        num = int(input("Choose a nummer between 1 and 3: "))
        if num == chance:
            print("Extraction successfull!")
            new_name = input("Please bestow the shadow a name: ")
            monster.name = new_name
            self.shadows += [monster.name]
        else:
            Hero.monster_disintegrated(self, monster)


    def kill(self, monster):
        print(monster.name, "has been slayed by", self.name)
        choice = input("Want to extract shadow " + monster.name + " ? (y/n): ")
        if choice == "y":
            Hero.shadow_extraction(self, monster)
        else:
            print(monster.name, "disintegrated")



class Monster():
    def __init__(self, name, type, rank):
        self.name = name
        self.type = type
        self.rank = rank

class Shadow(Monster):
    def __init__(self, name, type, rank, abilities, level):
        Monster.__init__(self, name, type, rank)
        self.abilities = abilities
        self.level = level

# create Hero
jinwoo = Hero("Jinwoo", "Dragontooth", "S", 107, [])

# create Monster
monster1 = Monster("monster1", "Humanoid", "A")

# Hero kills a Monster
jinwoo.kill(monster1)

print(jinwoo.shadows)



"""""
# create shadows
igris = Shadow("Igris", "Humanoid", "S+", ["Telekinesis", "Regeneration", "Conversation"], 100)
tank = Shadow("Tank", "Bear", "A+", ["Clawmark", "Buff", "Strength"], 80)
beru = Shadow("Beru", "Monster-Ant", "S+", ["Conversation", "Hardener", "Killsight"], 100)
"""""



