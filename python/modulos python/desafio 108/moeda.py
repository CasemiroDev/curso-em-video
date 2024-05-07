def dobro(a):
    b = a * 2
    return b

def metade(a):
    b = a / 2
    return b

def aumentar(a):
    b = a * 1.10
    return b

def diminuir(a):
    b = a * 0.90
    return b

def moeda(a, moeda = 'R$'):
    return f'{moeda}{a:>.2f}'.replace('.',',')
    
