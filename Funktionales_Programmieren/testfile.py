import itertools

for x in itertools.count(3,2):
    print(x)
    if x > 100:
        break
