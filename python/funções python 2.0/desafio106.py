def ajuda(com):
    help(com)

while True:
    resp = str(input("Precisa de ajuda? (S/N) ")).strip().upper()[0]
    if resp != 'S':
        break
    com = str(input("Qual comando você deseja ver o manual? "))
    ajuda(com)