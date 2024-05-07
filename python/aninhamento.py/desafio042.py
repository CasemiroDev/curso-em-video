lado1 = float(input("Digite o valor de um lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("O terceiro lado agora: "))

if lado1 == lado2 and lado1 == lado3 and lado3 == lado2 :
    print("É um triângulo Equilatero")
elif lado1 == lado2 and lado1 != lado3 and lado3 != lado2 :
    print("É um triângulo Isóceles")
elif lado1 != lado2 and lado1 == lado3 and lado3 != lado2 :
    print("É um triângulo Isóceles.")
elif lado1 != lado2 and lado1 != lado3 and lado3 == lado2 :
    print("É um triângulo isóceles.")
elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2 :
    print("É um triângulo Escaleno.")
else :
    print("Não forma um triângulo.")