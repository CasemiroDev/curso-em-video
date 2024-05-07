from datetime import datetime
dados = dict()
dados['nome'] = str(input("Digite seu nome: "))
nasci = int(input("Digite o ano em que você nasceu: "))
dados['idade'] = datetime.now().year - nasci
dados['ctps'] = int(input("Digite sua carteira de trabalho (0 para não): "))
if dados['ctps'] != 0:
    dados['contratação'] = int(input("Digite o ano de sua contratação: "))
    dados['salário'] = float(input("Digite seu salário: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for c, v in dados.items():
    print(f" - {c} tem o valor de {v}")