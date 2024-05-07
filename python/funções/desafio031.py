dist = float(input("Digite a distância da viagem: "))
if dist <= 200.0 :
    dist2 = dist * 0.50
    print("O preço da passagem será de {:.2f} reais".format(dist2))
else :
    dist3 = dist * 0.45
    print("O preço da viagem será de {:.2f} reais".format(dist3))