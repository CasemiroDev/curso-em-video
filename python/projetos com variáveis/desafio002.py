dist = float(input("Qual a quilometragem que você percorreu? "))
dias = float(input("Quantos dias o carro foi usado? "))
km = dist * 0.15
day = dias * 60
total = km + day
print("Você deve pagar: R$",total)