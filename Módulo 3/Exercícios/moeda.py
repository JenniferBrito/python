# ex107, 108, 109, 110
def dobro(n, m=False):
    d = n *2
    if m == True:
        result = moeda(d)
        return result
    else:
        return d

def metade(n, m=False):
    met = n / 2
    if m == True:
        result = moeda(met)
        return result
    else:
        return met


def aumentar(n, p, m= False):
    valor_final = n + (n * (p / 100))
    if m == True:
        result = moeda(valor_final)
        return result
    else:
        return valor_final

def diminuir(n, p, m=False):
    valor_final = n - (n * (p / 100))
    if m == True:
        result = moeda(valor_final)
        return result
    else:
     return valor_final

def moeda(n):
    v = str(n)
    v.replace('.', ',')
    form = f'R$ {v}'
    return form

def resumo(p, a, d,):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<15}{moeda(p):>15}')
    print(f'{"Dobro do preço:":<15}{dobro(p, True):>17}')
    print(f'{"Metade do preço:":<15}{metade(p, True):>15}')
    print(f'{"{a} do preço:":<15}{aumentar(p, a, True):>15}')
    print(f'{"{d} sdo preço:":<15}{diminuir(p, d, True):>15}')