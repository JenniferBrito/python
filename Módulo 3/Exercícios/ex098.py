# ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. 
# Seu programa tem que realizar 3 contagens através da função criada: 
#   a - de 1 até 10, de 1 em 1, 
#   b - de 10 até 0, de 2 em 2,
#   c - uma contagem personalizada

from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('Fim')
    
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
print()
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)