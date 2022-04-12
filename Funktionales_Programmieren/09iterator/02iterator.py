# Iteratoren geben

liste = [40,30,20,10]
iterator = liste.__iter__()
print(iterator)

print(next(iterator))
print(iterator.__next__())

# Beide Varianten sind das gleiche!

liste2 = [1,2,3,4]
for i in iter(liste2):
    print(i)

# Analog zu
for i in liste2:
    print(i)

