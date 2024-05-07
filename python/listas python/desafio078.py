lista = list()
val = maior = menor = 0
loc1 = loc2 = c = f = 0

for c in range(1,6):
    val = int(input(f"Digite o {c}ª valor: "))
    lista.append(val)

    if c == 1:
        menor = val

    if val > maior:
        maior = val
        loc1 = c

    if val < menor:
        menor = val
        loc2 = c



print(f"O maior valor digitado foi: {maior}, o menor valor foi {menor} e a localização de cada um é respectivamente {loc1},{loc2}")