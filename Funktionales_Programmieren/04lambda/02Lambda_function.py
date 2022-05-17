def quadrat_umfang(seitenlaenge: int) -> int:
    return seitenlaenge * 4

result1 = quadrat_umfang(10)

# Lambda ist eine Anonyme Funktion die kein Namenszuweisung benoetigt
result2 = (lambda x : x * 4)(10)


print(result1, result2)

