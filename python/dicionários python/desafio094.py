lista = list()
cont = 1
contM = 0
soma = 0
media = 0
contacima = 0
while True:
    pessoa = {'nome': str(input("Digite o nome de uma pessoa: ")),
              'sexo': str(input("Digite o sexo da pessoa: ")).strip().upper()[0],
              'idade': int(input("Digite a idade da pessoa: ")) 
}
    lista.append(pessoa)
    resp = str(input("Deseja continuar? (S/N) ")).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        contM += 1
    soma += pessoa["idade"]
    if pessoa["idade"] >= 40:
        contacima += 1
    if resp != 'S':
        break
    cont += 1
print("-="*30)
s = 0
for c in enumerate(lista):
    print(lista[s])
    s +=1
media = soma / cont
print("=-"*30)
print(f"O total de pessoas cadastradas foram {cont}")
print(f"Foram cadastradas {contM} mulheres.")
print(f"A média de todas as idades cadastradas é {media} anos")
print(f"A quantidade de pessoas acima de média em idade é {contacima}")
