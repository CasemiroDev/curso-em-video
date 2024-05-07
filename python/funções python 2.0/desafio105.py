def notas(*n, sit=False):
    """
    -Esta função irá calcular o boletim de uma turma, mostrando a situação dela.
    :*n: Diversas notas que a função irá receber
    :sit: Se deseja visualizar a situação de padrão ela vem :False:
    :return:
    """
    f = dict()
    f['quant'] = len(n)
    f['maior'] = max(n)
    f['menor'] = min(n)
    f['media'] = sum(n)/len(n)
    if sit == True:
        if f['media'] >= 7.0:
            f['situação'] = "BOA"
        elif f['media'] >= 5.0:
            f['situação'] = "RECUPERAÇÃO"
        else:
            f['situação'] =  "REPROVAÇÃO"
    return(f)

boletim = notas(8.5,6.4,8.4,9.5,sit=True)
print(boletim)
#help(notas)
