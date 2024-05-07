import random
sort = random.randint(0,10)
num = int(input("Digite um número até ganhar da máquina: "))
tent = 1
while num != sort:
    num = int(input("Tente novamente: "))
    tent += 1
print(f"Você ganhou com {tent} tentativas.")
