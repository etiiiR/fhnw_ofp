# Eine Funktion hat einen Namen und kann mehrere Parameter beinhalten
# Eine Funktion kann entweder einen Rueckgabewert haben oder direkt etwas ausgeben
# Eine Funktino kann man mehrmals aufrufen

# Funktion vol definieren
def vol(radius: int) -> int:
    """
    :param radius: Radius der Kugel
    :return: Volumen der Kugel
    """
    return radius ** 3 * 3.14 * 4 / 3
print(vol(10))

# Anonyme Funktion mit Lambda (Hat keinen Namen -> Anonym)
print((lambda x: x ** 3 * 3.14 * 4 / 3)(10))
