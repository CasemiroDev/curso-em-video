salar = float(input("Digite seu salário: "))
if salar <= 1250.0 :
    neosalar = salar * 1.15
else :
    neosalar = salar * 1.10
print("Seu novo salario é",neosalar,"em reais")