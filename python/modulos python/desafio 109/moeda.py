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
    
