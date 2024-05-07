idade = int(input("Atleta, qual é sua idade? "))
if idade <= 9 :
    print("MIRIM")
elif idade >9 and idade <= 14 :
    print("INFANTIL")
elif idade >14 and idade <= 19 :
    print("JÚNIOR")
elif idade >19 and idade <= 25 :
    print("SÊNIOR")
elif idade >25 :
    print("MASTER")