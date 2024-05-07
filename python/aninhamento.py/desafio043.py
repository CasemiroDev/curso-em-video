altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso corporal: "))

imc = peso / (altura**2)

if imc < 18.5 :
    print("Você está abaixo do peso ideal")
elif imc == 18.5 or imc <= 25.0 :
    print("Você está no peso ideal.")
elif imc > 25.0 or imc <= 30.0 :
    print("Você está com sobrepeso")
elif imc > 30.0 or imc <= 40 :
    print("Você tem obesidade.")
elif imc > 40.0 or imc < 100.0 :
    print("Você tem obesidade mórbida.")
else :
    print("Você não é humano.")

print("seu imc é {:.2f}".format(imc))