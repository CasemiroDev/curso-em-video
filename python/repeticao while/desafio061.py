from time import sleep
print("=-" * 12)
sleep(1)
print("Gerador de PA")
sleep(1)
print("=-" * 12)
sleep(1)

pt = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1
print(pt,"",end="")
sleep(1)
while cont != 10:
    pt += razao
    print(pt,"",end="")
    cont += 1
    sleep(1)
print("fim!")