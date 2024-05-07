num = int(input("Digite um número: "))
num2 = 1
print(f"{num}! = ",end="")
while num != 1:
    num2 *= num
    print(num,"x ",end="")
    num -= 1
   
print(f"1 = {num2}")


    