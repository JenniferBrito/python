# ex028: Escreva um programa que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)

palpite = int(input('Digite seu palpite entre 0 e 5: '))

print('O número gerado é: {}'.format(num))
if palpite == num:
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente outra vez.')