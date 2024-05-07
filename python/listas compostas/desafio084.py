maior = menor =  0
cont = ""
temp = list()
comp = list()

while True:
    temp.append(str(input("Digite seu nome: ")))
    temp.append(int(input("Digite seu peso: ")))
    
    if len(comp) == 0:
        maior = temp[1]
        menor =temp[1]
    
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    comp.append(temp[:])
    temp.clear()

    cont= str(input(("Deseja continuar? [S/N] "))).strip().upper()[0]
    if cont == "N":
        break

print(f"Os dados armazenados foram {comp}")
print("Ao todo foram feitos", len(comp),"registros")
print(f"O maior peso arquivado foi {maior}. Peso de: ",end="")
for p in comp:
    if p[1] == maior:
        print(f"{p[0]}",end=" ")
print("")
print(f"O menor peso arquivado foi {menor}. Peso de: ",end="")
for p in comp:
    if p[1] == menor:
        print(f"{p[0]}",end=" ")
print("")

