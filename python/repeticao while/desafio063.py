num = int(input("Digite quantos termos da sequência você deseja visualizar: "))
num2 = 2
fator1 = 0
fator2 = 1
print("0 -> 1 -> ",end="")
while num2 < num:
    fator3 = fator1 + fator2
    print(fator3,"-> ",end="")
    fator1 = fator2
    fator2 = fator3


    num2 += 1
print("fim!")