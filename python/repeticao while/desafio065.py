maior = menor = soma = num = cont =0
resp = "S"
while resp == "S":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else :
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input("Deseja continuar? ").strip().upper()[0]
media = soma / cont
print(f"foram digitados {cont} valores e a média entre eles é {media}.")
print(f"o maior número é {maior} e o menor é {menor}.")
    

