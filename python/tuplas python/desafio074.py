from random import randint
numbers = list()
cont = 0
for c in range (1,5):
    number = randint(1,10)
    numbers.append(number)
    cont+= 1
print(tuple(numbers))
print(f"Foram escolhidos {cont} números")
print("barbecue bacon burguer")
