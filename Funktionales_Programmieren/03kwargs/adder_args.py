def adder(*args):
    print(type(args))

    sum = 0

    for n in args:
        sum += n
    print("Summe ist:", sum)

adder(3,2,5)
adder(2,5,3,3,5,3)

# *args sind spezielle keyword Argumente fuer Funktionen
# *args Argumente werden in Form von **Tupple** weiter gegeben
# *args Argumente koennen beliebige lang sein
# *args Argumente machen die Funktion flexibler