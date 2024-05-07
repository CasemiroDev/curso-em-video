def dobro(a, format = False):
    b = a * 2
    return b if format == False else moeda(b)

def metade(a, format = False):
    b = a / 2
    return b if format == False else moeda(b)

def aumentar(a, format = False):
    b = a * 1.10
    return b if format == False else moeda(b)

def diminuir(a, format = False):
    b = a * 0.90
    return b if format == False else moeda(b)

def moeda(a, moeda = 'R$'):
    return f'{moeda}{a:>.2f}'.replace('.',',')

def resumo(a, format=True):
    print(f"O dobro de {a} é {dobro(a, format=True)}")
    print(f"A metade de {a} é {metade(a, format=True)}")
    print(f"Aumentando 10% de {a} temos{aumentar(a, format=True)}")
    print(f"Diminuindo 10% de {a} temos {diminuir(a, format=True)}")