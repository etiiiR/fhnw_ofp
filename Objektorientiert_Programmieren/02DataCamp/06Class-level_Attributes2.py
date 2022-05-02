class Player:
    MAX_SPEED = 3

p1, p2 = Player(), Player()

print("printing max speed of p1, p2: ", p1.MAX_SPEED, p2.MAX_SPEED)

# Changing Max Speed to 7 for p1 Object
p1.MAX_SPEED = 7

print("printing max speed after change: ", p1.MAX_SPEED, p2.MAX_SPEED)

# Didnt change globaly
print("didnt change MAX_SPEED globaly:", Player.MAX_SPEED)

# To change to variabel MAX_SPEED we use
Player.MAX_SPEED = 7

print("Now its changed globaly:", Player.MAX_SPEED)