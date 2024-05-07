num = 0
tab = 1
chose = 1
while num >= 0:
    num = int(input("Digite um número para ver sua tabuada: "))
    if num < 0:
        break
    print("tabuada: ")
    for c in range(0,10):
        num2 = num * tab
        print(f"{num} x {tab} = {num2}")
        tab += 1
print("Programa encerrado")
    
    