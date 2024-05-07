sexo = input("Digite seu sexo: ").strip().upper()[0]
while sexo not in "MmFf":
    sexo = input("Dados inválidos, por favor digite seu sexo: ").strip().upper()[0]
print(f"Sexo {sexo} arquivado com sucesso.")
