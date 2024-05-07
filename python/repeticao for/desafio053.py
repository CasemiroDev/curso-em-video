name = str(input("Digite uma frase: ")).strip()

name = ''.join(name.split())

count = name[::-1]

if name == count :
    print("é um palindromo")
else :
    print("Não é um palindromo")
