valores = ("Lápis", 1.30,
           "Borracha", 2.0,
           "Caneta", 1.50,
           "Caderno", 20.0)
c = 0
for c in range(0,len(valores)):
    if c % 2 == 0:
        print(f"{valores[c]:.<30}",end="")
    else:
        print(" ",f"{valores[c]:>5.2f}")