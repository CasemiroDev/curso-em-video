import moeda
a = int(input("Digite o preço: R$"))
print(f"O dobro de {moeda.moeda(a)} é igual a {moeda.moeda(moeda.dobro(a))}")
print(f"A metade de {moeda.moeda(a)} é igual a {moeda.moeda(moeda.metade(a))}")
print(f"{moeda.moeda(a)} aumentado em 10% é {moeda.moeda(moeda.aumentar(a))}")
print(f"Diminuindo {moeda.moeda(a)} em 10% temos {moeda.moeda(moeda.dobro(a))}")

