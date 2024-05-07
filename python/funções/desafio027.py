ano = float(input("Digite um número: "))
if ano % 4 == 0 and ano % 100 != 0 and ano %  400 != 0 :
    print("O ano é bissexto!")
else :
    print("O ano não é bissexto")
