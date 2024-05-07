print("=" * 30)
print("10 Primeiros termos de uma PA")
print("=" * 30)

termo = int(input("Qual o primeiro termo? "))
razao = int(input("Qual é a razão? "))

for c in range(termo, termo + 10 * razao, razao):
    print("{}".format(c),end=" -> ")
print("Acabou")