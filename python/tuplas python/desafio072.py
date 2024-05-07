cont2 = int(input("Digite o número que você deseja ver por extenso: "))
extensao = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezeseis","dezesete","dezoito","dezenove","vinte")
for cont,c in enumerate(extensao):
    if cont2 == cont:
        print(c)
print("fim!")





