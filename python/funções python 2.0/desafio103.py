def ficha(jog = '<desconhecido>',gols = 0):
    print(jog,"fez",gols,"gols.")

n = str(input("Digite o nome do jogador: "))
g = str(input("Digite a quantia de gols do jogador: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.isnumeric():
    n = '<desconhecido>'
if n.strip == "":
    ficha(jog=n)
else:
    ficha(n,g)