def fatorial(a = 1, show = False):
    """
    - Este Programa irá calcular o fatorial de um número.
    :param a: O número que você deseja ver o fatorial.
    :param show: Se você deseja visualizar todos os números que fazem parte do fatorial.
    :return:
    """
    f=1
    print(f"O fatorial de {a} é: ",end="")
    for c in range(a,0,-1):
        if show == True:
            if c > 1:
                print(c,"x ",end="")
            else:
                print("1 = ",end="")
        f *= c
    return f
print(fatorial(5))
help(fatorial)