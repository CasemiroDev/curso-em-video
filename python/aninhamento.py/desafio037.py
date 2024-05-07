num = int(input("Digite um número inteiro: "))
print("Digite 1 para binário.")
print("Digite 2 para octal.")
print("Digite 3 para hexadecimal.")
base = int(input(""))

if base == 1 :
    num2 = bin(num)
    print("O número binário fica:",num2)
elif base == 2 :
    num3 = oct(num)
    print("O número octal fica:",num3)
elif base == 3 :
    num4 = hex(num)
    print("O número hexadecimal fica:",num4)
else :
    print("Digite um número entre 1 e 3 e tente novamente.")
