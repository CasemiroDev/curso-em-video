import random
num1 = input("Primeiro nome: ")
num2 = input("Segundo nome: ")
num3 = input("Terceiro nome: ")
num4 = input("Quarto nome: ")
list = [num1,num2,num3,num4]
random.shuffle(list)
print(list)