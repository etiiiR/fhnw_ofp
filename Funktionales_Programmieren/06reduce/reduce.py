# Reduce braucht eine Funktion mit 2 Parameter, 1 Liste und 1 Startwert
# erster Parameter bezieht sich auf Startwert
# zweiter Parameter bezieht sich auf Element in der Liste
# erster Parameter ist der Startwert der sich immer aendert. und a ist immer das letzte vorhherige Resultat.

liste = [1,2,3,5]

from functools import reduce
print(reduce(lambda a, b: a + b+1, liste, 0))


summe = 0
for i in liste:
    summe += i+1
    print(summe)



def mein_filter(func, liste):
    return reduce(lambda a, b: a + [b] if func(b) else a, liste, [])

a = mein_filter(lambda x: x > 4, [1,2,3,4,5,6,7,8])
print(a)

