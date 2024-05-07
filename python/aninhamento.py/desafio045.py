import random
print("Bem vindo ao Jokenpô!")
print("Suas opções:")
print("[ 1 ] Pedra")
print("[ 2 ] Papel")
print("[ 3 ] Tesoura")
joga = int(input("Qual é sua jogada? "))
x = random.randint(1,3)

if x == 1 :
    print("Máquina joga pedra.")
if x == 2 :
    print("Máquina joga papel.")
if x == 3 :
    print("Máquina joga tesoura.")

if joga == 1 and x == 3 :
    print("Jogador vence!")
elif joga == 1 and x == 2 :
    print("Jogado perde.")
elif joga == 1 and x == 1 :
    print("Jogador empata")

if joga == 2 and x == 1 :
    print("Jogador vence!")
elif joga == 2 and x == 2 :
    print("Jogador empata.")
elif joga == 2 and x == 3 :
    print("jogador perde.")

if joga == 3 and x == 1 :
    print("Jogador perde.")
elif joga == 3 and x == 2 :
    print("Jogador ganha!")
elif joga == 3 and x == 3 :
    print("Jogador empata.")

