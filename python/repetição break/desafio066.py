cont = soma = 0
print("Digite 999 para sair.")
while True:
    num = int(input(f"Digite o {cont + 1}ª número:"))
    if num == 999:
        break
    cont+=1
    soma += num

print(f"Foram digitados {cont} números e a soma entre eles é {soma}.")