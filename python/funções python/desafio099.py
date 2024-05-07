def maior():
    maior = cont = a = 0
    resp = "S"
    while resp == "S":
        a = int(input("Digite um número de 0 a 100: "))
        if cont == 0:
            maior = a
        elif a > maior:
            maior = a
        cont += 1
        resp = str(input("Deseja continuar? (S/N) ").strip().upper()[0])
    print(f"O maior número digitado foi {maior}")
maior()

