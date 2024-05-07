num = 0
c = 1
lista = list()

while True:
    num = int(input(f"Digite o {c}ª número: "))
    c += 1
    if num in lista:
        break
    lista.append(num)

print("Você digitou um número que já havia sido digitado antes")
print("A ordem dos números digitados é: ", sorted(lista))
    