# ex100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre os valores pares sorteados pela função anterior.

from random import randint

lista = list()

def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))

def somaPar(lst):
    result = 0
    for c in lst:
        if c % 2 == 0:
            result += c
    print(f'A soma de todos os valores pares é: {result}.')

sorteio(lista)
print(f'A lista sorteada é: {lista}')
somaPar(lista)