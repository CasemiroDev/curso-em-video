num1 = float(input("Digite o comprimento do cateto oposto: "))
num2 = float(input("Digite o comprimento do cateto adjacente: "))
hip1 = num1 ** 2
hip2 = num2 ** 2
hip3 = hip1 + hip2
hipotenusa = hip3**0.5
print("A hipotenusa é {:.2f}".format(hipotenusa))