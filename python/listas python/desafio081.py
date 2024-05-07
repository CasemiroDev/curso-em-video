lista = list()
lista2 = list()
n = int(input("Digite quantos números você deseja digitar: "))

for c in range(1,n+1):
    num = int(input(f"Digite o {c}ª número: "))
    lista.append(num)

lista2 = sorted(lista ,reverse=True)

if 5 in lista:
    print(f"Foram digitados {n} valores, a lista de forma decrescente é: {lista2} e o valor 5 foi digitado")
else: 
    print(f"Foram digitados {n} valores, a lista de forma decrescente é: {lista2} e o valor 5 não foi digitado")