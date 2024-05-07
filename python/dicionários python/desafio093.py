jogador = {'nome': str(input("Digite o nome do jogador: ")),
           'partidas': int(input(f"Digite a quantidade de partidas: "))
           }
a = 0
temp = 0
for c in range(1,jogador['partidas'] + 1):
    temp = int(input(f"Digite a quantidade de gols do {c} jogo: "))
    a += temp
jogador["gols"] = a
print(f"O jogador se chama {jogador['nome']}, tem {jogador['partidas']} partidas, com um total de {jogador['gols']}")
