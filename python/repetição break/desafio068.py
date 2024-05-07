from random import randint
trye = sort = cont =0
while True:
    resp = input("Par ou impar: ").strip().upper()[0]
    if resp == "Í" or resp == "I" or resp == "i" or resp == "í":
        num = 2
    elif resp == "p" or resp == "P":
        num = 1
    sort = randint(0,10)
    trye = int(input("Digite um número: "))
    rest = sort + trye
    if rest % num == 0:
        cont += 1
        print("ganhaste essa!")
    else:
        break
print(f"Você perdeu. ganhando um total de {cont}")