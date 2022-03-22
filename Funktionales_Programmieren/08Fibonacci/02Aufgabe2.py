## Aufgabe 2

# Funktion die 1 Parameter braucht und 2 Rueckgabewerte

def fibonacci_rec(n: int):

    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

print(fibonacci_rec(2))