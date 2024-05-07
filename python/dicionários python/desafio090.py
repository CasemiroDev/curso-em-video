united = dict()
united["nome"] = str(input("Digite o nome do aluno: "))
united["media"] = float(input("Digite a média do aluno: "))
print("-="*20)
print("O nome do aluno(a) é:",united["nome"])
print(f"A média de {united['nome']} é:",united["media"])
if united["media"] >= 7.0:
    print("A situação do aluno é: Aprovado")
elif united["media"] < 7.0 >= 4.0:
    print("A situação do aluno é: Recuperação")
else:
    print("A situação do aluno é: Reprovado")
