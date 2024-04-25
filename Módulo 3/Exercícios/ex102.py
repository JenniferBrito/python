# ex102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular 
# e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):

    # A importação de uma biblioteca pode ser feita dentro de uma def
    # dessa forma não será possível acessá-la em outro local dentro do programa

    from math import factorial 
    c = num
    fat = 1

    if show == True:
        while c > 0:
            print('{}'.format(c), end='')
            print(' x ' if c > 1 else ' = ', end='')
            fat = factorial(num)
            c -= 1
        print(fat)
    else:
        fat = factorial(num)
        print(fat)

fatorial(5)
fatorial(5, True)
