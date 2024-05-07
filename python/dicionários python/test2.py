lista1 = []
lista2 = []
num = 0
for c in range(0,5):
    num = int(input("Digite um valor: "))
    lista1.append(num)
    print(lista1)
    lista2.append(lista1[:])
    lista1.clear()
print(lista1)
print(lista2)
print(num)
