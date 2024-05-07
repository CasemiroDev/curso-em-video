from random import randint
templist = 0
lista = list()

print("-"*30)
print("     JOGA NA MEGA SENA      ")
print("-"*30)
resp = int(input("Quantos jogos você quer que eu sorteie? "))
for c in range(0,resp):
    for f in range(1,7):
        templist = randint(0,99)
        lista.append(templist)
    print(f"Jogo {c+1}: ",lista)
    lista.clear()
print("-=-==-=-=-=-=-=-> Boa Sorte <-=-=-=-=-=-=-=-")



