
def dobro(n = 0, m=False):
    d = n *2
    return d if m is False else moeda(d)


def metade(n = 0, m=False):
    met = n / 2
    return met if m is False else moeda(met)

def aumentar(n = 0, p = 0, m= False):
    valor_final = n + (n * (p / 100))
    return valor_final if m is False else moeda(valor_final)

def diminuir(n = 0, p = 0, m=False):
    valor_final = n - (n * (p / 100))
    return valor_final if m is False else moeda(valor_final)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:>.2f}'.replace('.', ',')

def resumo(p = 0, a = 10, d = 5):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço:\t{metade(p, True)}')
    print(f'{a} por cento do preço: \t{aumentar(p, a, True)}')
    print(f'{d} pot cento do preço: \t{diminuir(p, d, True)}')