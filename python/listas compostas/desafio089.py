temp = []
lista = []
mediatemp = []
nome = []
media = []
n = 0
resp = resp2 = ""

n = int(input("Quantos aluno tem na turma? "))
for c in range(0,n):
    temp.append(str(input(f"Digite o nome do {c+1}ª aluno: ")))
    temp.append(float(input(f"Digite a primeira nota do {c+1}ª aluno: ")))
    temp.append(float(input(f"Digite a segunda nota do {c+1}ª aluno: ")))
    mediatemp.append((temp[1] + temp[2]) / 2)
    media.append(mediatemp[:])
    nome.append(temp[0])
    temp.clear()
    mediatemp.clear()
    
print("BOLETIM","-="*18)
for c in range(0,n):
    if c == 0:
        print(c + 1,nome[0],"."*20,media[0])
    else:
        print(c + 1,nome[c],"."*20,media[c])
print("-="*22)

resp = str(input("Deseja ver sua nota individual? [S/N] ")).strip().upper()
if resp == "S" or resp == "s":
    resp2 = int(input("Qual seu número na chamada? "))
    print(nome[resp2 - 1],"."*20,media[resp2 - 1])
print("Término do programa","-=" * 12)



