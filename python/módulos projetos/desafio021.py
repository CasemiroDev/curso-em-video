frase = str(input("Digite uma frase: ")).strip()
frase.lower()
frase1 = frase.count("a")
print("A frase tem",frase1,'a')

frase2 = frase.split()
frase3 = frase2[0].find("a")+1
print("a primeira instância do a é no",frase3,"letra")
frase4 = frase.rfind("a")+1
print("o último a fica no",frase4,"local")
 
