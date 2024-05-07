def contador(i,f,c):
    print(f"Contador de {i} a {f} de {c} em {c}.")
    if i > f:
        while i > f+1:
            print (i,", ",end="")
            i -= c
        print("fim!")
    elif i < f:
        while i < f+1:
            print(i,", ",end="")
            i += c
        print("fim!")
contador(1,10,1)
contador(10,0,2)
print("=-"*20)
i = int(input("Digite o número de início da contagem: "))
f = int(input("Digite o último número da contagem: "))
c = int(input("Digite o valor de número em número que será contado: "))
contador(i,f,c)
