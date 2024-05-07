from time import sleep
num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
choice = 0
while choice != 5 :
    print("=-" * 20)
    print("Menu de interações")
    print("O que você deseja fazer?")
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    print("=-" * 20)
    choice = int(input("Escolha uma das opções: "))
    if choice == 1:
        num3 = num + num2
        print(f"A soma entre os dois é de {num3}.")
        sleep(5)
    elif choice == 2:
        num4 = num * num2
        print(f"O produto entre os dois é de {num4}.")
        sleep(5)
    elif choice == 3:
        if num > num2:
            print(f"O valor {num} é o maior entre os dois.")
            sleep(5)
        elif num < num2:
            print(f"O valor {num2} é o maior entre os dois.")
            sleep(5)
        else :
            print("Os dois valores são iguais.")
            sleep(5)
    elif choice == 4 :
        num = int(input("Digite o primeiro novo valor: "))
        num2 = int(input("Digite o segundo novo valor: "))
        sleep(5)
print("Você decidiu sair do programa.")