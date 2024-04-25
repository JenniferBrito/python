# ex020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos. 
# Faça um programa que leia os nomes e mostre a ordem sorteada

from random import sample

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')

lista = [n1, n2, n3, n4]
sorteio = sample(lista, k=4)

print('A ordem sorteada é {}'.format(sorteio))