num = 0
num2 = 0
for c in range(0, 6):
    num = int(input("Digite um número: "))
    if num % 2 == 0 :
        num2 += num
print("A soma de todos os números é:",num2)