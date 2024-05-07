val = (int(input("Digite o primeiro número: ")),
       int(input("Digite o segundo número: " )),
       int(input("Digite o terceiro número: ")),
       int(input("Digite o quarto número: ")))
cont = val.count(9)

print("A quantidade de vezes que apareceu o valor 9 foi: ",cont)
if 3 in val:
    print("A posição do primeiro número três foi: ",val.index(3)+1)
else:
    print("O valor 3 não está em nenhuma posição.")
print("Os valores pares digitados foram: ",end="")
for n in val:
    if n % 2 == 0:
        print(n,end=" ")
