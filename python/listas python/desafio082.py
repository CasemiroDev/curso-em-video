lista1 = list()
lista2 = list()
lista3 = list()
n = int(input("Digite quantos números você deseja digitar: "))
for c in range(1,n+1):
    num = int(input(f"Digite o {c} número: "))
    lista1.append(num)
    
    if num % 2 == 0:
        lista2.append(num)
    
    else:
        lista3.append(num)

print(f"A primeira lista total é {lista1}, a lista de pares é {lista2} e a lista de ímpares é {lista3}")