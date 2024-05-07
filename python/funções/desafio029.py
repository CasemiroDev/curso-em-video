vel = float(input("Digite a velocidade do carro: "))
if vel > 80.0 :
    print("O carro foi multado")
    val = vel - 80.0
    val2 = val * 7.0
    print("A multa foi de {:.2f} reais".format(val2))
else :
    print("O carro não foi multado")
