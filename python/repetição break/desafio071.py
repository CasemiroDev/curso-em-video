val = int(input("Digite o valor a ser sacado (inteiro): "))
cont1 = cont2 = cont3 = cont4 = val2 = val3 = val4 = val5 = 0
while val != 0:
    if val >= 50 and val < 10000 :
        val -= 50
        cont1 += 1
    if val < 50 and val >= 20 :
        val -= 20
        cont2 += 1
    if val < 20 and val >= 10 :
        val -= 10
        cont3 += 1
    if val < 10 and val >= 1:
        val -= 1
        cont4 += 1
print(f"Foram sacas {cont1} notas de 50, {cont2} notas de 20, {cont3} notas de 10 e {cont4} notas de 1.")