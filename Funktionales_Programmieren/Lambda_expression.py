# Anonymous Functions = Lambda Expressions

lambda x: 3*x + 1 # Allgemeine Struktur von Lambda

g = lambda x: 3*x # Der Lambda Function eine Variabel zuweisen
print(g(2))

# Combine first and last name into single Full name
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name(" LeonharD   ", "  EUler"))
# strip() -> Entfernt die Leerschlaege
# title() -> Erster Buchstabe ist immer gross, alle anderen klein

# not giving a name
scifi_authors = ["isax Newton", "Ray Brandenburg", "Rober Douglas", "Artuhs Johnsen"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
# sort() -> Nimmt 2 Argumente, key=None, und reverse=True oder reverse=False
# split(" ") Durch das Split, trenne ich die Leerschlaege, ["isax","Newton"]
# [-1] durch das -1 wird das letzte Wort genommen
# durch .lower() werden die Woerter komplett klein geschrieben, um nicht aufrund Gross Klein zu sortieren

# Quadratic Functions
def build_quadratic_function(a,b,c):
    "Returns the function f(x) = ax^2 + bx + c"
    return lambda x: a*x**2 + b*x + c
# Eine Funktion wird zurueckgegeben!

function_f = build_quadratic_function(10,30,10)
print(function_f(10))

# Ohne eine Variabel Zuweisung
print(build_quadratic_function(10,30,10)(10))
