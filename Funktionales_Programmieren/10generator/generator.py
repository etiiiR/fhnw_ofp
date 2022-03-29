x = [10,20,304,503]



def fun(liste):
    for x in liste:
        yield x

a = fun(x)
print(a)

print(a.__next__())

for i in a:
    print(i)


# Generator ist eine Implementierung des Iteratrs
# Generator ist eine Funktion der einen Iterator zurueckgibt, und der Iterator gibt den Wert zurueck.



