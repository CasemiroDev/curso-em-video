import moeda
a = int(input("Digite o preço: R$"))
print(f"O dobro de {moeda.moeda(a)} é igual a {moeda.dobro(a, True)}")
print(f"A metade de {moeda.moeda(a)} é igual a {moeda.metade(a, True)}")
print(f"{moeda.moeda(a)} aumentado em 10% é {moeda.aumentar(a, True)}")
print(f"Diminuindo {moeda.moeda(a)} em 10% temos {moeda.dobro(a)}")

