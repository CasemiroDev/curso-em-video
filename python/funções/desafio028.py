import random
num = random.randint(0,5)
sort = int(input("tente adivinhar o número que a máquina escolheu de 0 a 5: "))
if sort == num :
    print("Parabéns você ganhou!")
else :
    print("A máquina venceu...")    
print(num)