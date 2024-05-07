lista = list()
lista2 = list
maior = menor = 0
for c in range(1,6):
    num = int(input(f"Digite o {c}ª número: "))
    lista.append(num)
lista2 = sorted(lista)
print(lista2)

