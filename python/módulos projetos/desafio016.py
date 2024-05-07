import random
num1 = input("Primeiro nome: ")
num2 = input("Segundo nome: ")
num3 = input("Terceiro nome: ")
num4 = input("Quarto nome: ")
lista = [num1,num2,num3,num4]
sort = random.choice(lista)
print("O aluno escolhido foi",sort)