resp = "S"
var1 = var2 = var3 = 0
nome = idade = sexo = ""
while resp == "S":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: (M/F) ").strip().upper()[0]

    if idade > 18:
        var1 += 1
    if sexo == "M":
        var2 += 1
    if sexo == "F" and idade > 20 :
        var3 += 1
    resp = input("Deseja continuar a digitar? ").strip().upper()[0]
print(f"Foram cadastradas {var1} pessoas com mais de 18 anos.")
print(f"Foram cadastradas {var2} pessoas do sexo masculino.")
print(f"{var3} pessoas são mulheres com mais de 20 anos")
