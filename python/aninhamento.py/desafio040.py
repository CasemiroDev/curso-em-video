nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5.0 :
    print("REPROVADO")
elif media >= 7.0 :
    print("APROVADO")
else :
    print("RECUPERAÇÃO")