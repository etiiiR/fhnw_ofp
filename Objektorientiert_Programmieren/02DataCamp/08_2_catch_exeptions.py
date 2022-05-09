def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")

a = [5,6,0,7]

print(invert_at_index(a, 1))

print(invert_at_index(a, 2))

print(invert_at_index(a, 5))