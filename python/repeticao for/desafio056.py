media = 0
media2 = 0
maior = 0
nomevelho = ""
totmulher = 0

for c in range(1,5) :
    nome = input(f"Digite o nome da {c}ª pessoa")
    idade = int(input(f"Digite a idade da {c}ª pessoa"))
    sexo = input(f"Digite o sexo da {c}ª pessoa")

    media += idade
    
    if c == 1 and sexo in "macho" :
        maior = idade
        nomevelho = nome
        if sexo == "macho" and idade > maior:
            maior = idade
            nomevelho = nome
    if sexo == "fêmea" and idade < 20:
        totmulher += 1
media2 = media / 4
print(f"A média de idade é {media2}")
print(f"A idade e nome do homem mais velho é {maior} e {nomevelho}")
print(f"Ao todo são {totmulher} mulheres com menos de 20 anos.")
