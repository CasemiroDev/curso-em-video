resp = "S"
nome = barato2 = ""
preco = preco2 = quant = cont = 0
caro = barato =  0

while resp == "S" :
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    cont += 1
    preco2 += preco

    if preco > 1000:
        quant += 1
    if cont == 1:
        barato = preco
        barato2 = nome

    if preco < barato:
        barato2 = nome
    
    resp = input("Deseja continuar digitando? (S/N) ").strip().upper()[0]
print(f"A soma total de preços é {preco2}")
print(f"{quant} produtos custam mais de 1000 reais")
print(f"o produto mais barato é o {barato2}")