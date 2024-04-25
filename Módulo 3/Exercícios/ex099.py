# ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos e dizer qual é o maior.

def maior(*valores):
    maior = 0
    if len(valores) == 0:
        print('A lista está vazia, não há valores a serem analisados.')
    else:
        for c in valores:
            if c > maior:
                maior = c
        print(f'O maior valor encontrado na lista {valores} é {maior}.')

maior(2, 5, 9, 1, 3)
maior(30, 48, 99)
maior(7, 9, 6, 4, 1, 108, 204, 10)
maior(6)
maior()