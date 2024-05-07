num = 1
cont = 0
end = 0
num2 = 0
while end != 999:
    num = int(input(f"Digite o {cont + 1}ª número: "))
    end = num
    cont += 1
    num2 += num
print(f"A quantia de números digitados foi {cont - 1} e a soma ente eles é {num2 - 999} ")
    