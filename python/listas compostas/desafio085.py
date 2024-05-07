tempnum = 0
impar1 = []
par1 = []
par2 = []
impar2 = []

for c in range(1,8):
    tempnum = int(input(f"Digite o {c}ª número: "))
    if tempnum % 2 == 0:
        par1.append(tempnum)
    if tempnum % 2 == 1:
        impar1.append(tempnum)

    par2 = sorted(par1)
    impar2 = sorted(impar1)


print("=-" * 30)
print("Os números pares foram", par2)
print("Os números ímpares foram", impar2)