resp = ""
gamer = []
individual = []
lista = []
temp = 0
while True:
    jogador = {'nome': str(input("Digite o nome do jogador: ")),
            'partidas': int(input(f"Digite a quantidade de partidas: "))
            }
    a = 0
    temp = 0
    for c in range(1,jogador['partidas'] + 1):
        temp = int(input(f"Digite a quantidade de gols do {c} jogo: "))
        individual.append(temp)
        a += temp
    lista.append(individual[:])
    individual.clear()
    jogador["gols"] = a
    gamer.append(jogador.copy())
    resp = str(input("Digite se deseja continuar a digitar mais jogadores: (S/N) ")).strip().upper()[0]
    if resp != "S":
        break

print("-="*30)
print("cod ",end="")
for p in jogador.keys():
    print(f"{p:<15}",end="")
print("")
print("-=" *20)
for c,v in enumerate(gamer):
    print(f"{c:<4}",end="")
    for d in v.values():
        print(f"{str(d):<15}",end="")
    print("")

print("-="*30)
while True:
    resp2 = str(input("Deseja ver o aproveitamento indivídual de algum jogador? (S/N) ")).strip().upper()[0]
    if resp2 != "S":
        break   
    else:
        while True:
            n = int(input("Qual o código do jogador que você deseja visualizar? "))
            while True:
                if n > len(gamer):
                    print("Esse código não existe")
                else:
                    break
            break
    print(f"Jogador {gamer[n]['nome']}",end="")
    print(f" fez os gols em ordem por jogo {lista[n]}")
    print(f"Sendo um total de {gamer[n]['gols']} gols")