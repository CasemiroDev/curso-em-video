def voto(ano):
    from datetime import date
    atualidade = date.today().year
    idade = atualidade - ano
    if idade > 15 and idade < 18 or idade >= 70:
        return f'Com {idade} - Voto Opcional'
    elif idade < 16:
        return f'Com {idade} - Não vota'
    else:
        return f'Com {idade} Voto obrigatório'

print(voto(2005))