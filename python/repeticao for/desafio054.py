name2 = 0
name3 = 0

for c in range(0, 7) :
    name = int(input("Digite em que ano você nasceu:"))
    if name > 2005 :
        name2 += 1
    elif name <= 2005 :
        name3 += 1
print("{} pessoas são de menor e {} são de maior.".format(name2,name3))