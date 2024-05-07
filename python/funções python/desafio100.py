from random import randint
numeros = []
def sorteia():
    for c in range(0,5):
        a = randint(0,10)
        numeros.append(a)
    print(numeros)
def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma entre todos os números pares é {soma}")
sorteia()
somaPar()
