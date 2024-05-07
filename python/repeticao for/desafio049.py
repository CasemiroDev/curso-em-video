soma = 0
cont = 0
for num in range(0, 6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print("A quantia de números que você digitou foi {} e a soma dos pares é {}".format(cont,soma))