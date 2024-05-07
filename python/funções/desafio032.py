num1  = int(input("Digite um número: "))
num2 = int(input("Dgite outro número: "))
num3 = int(input("Digite mais um número: "))

if num1 > num2 and num3:
    print("o maior número é o",num1)

if num2 > num1 and num2 > num3:
    print("o maior número é o",num2)

if num3 > num2 and num1:
    print("o maior número é o",num3)

menor = num1

if num2 < num1 and num3 :
    menor = num2

if num3 < num2 and num1 :
    menor = num3

print("o menor número é o",menor)
