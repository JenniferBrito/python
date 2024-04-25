# ex088: Faça um programa que ajude um jogador da mega sena a criar palpites. 
# O programa deverá perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

apostas = []
jogo = []

num = int(input('Quantas apostas você deseja fazer? '))

for c in range(0, num):
    for v in range(0, 6):
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
        else:
            jogo.append(randint(1, 60))
    apostas.append(jogo[:])
    jogo.clear()

for l in range(0, len(apostas)):
    apostas[l].sort()

for v in range(0, len(apostas)):
    print('='*35)
    print(f'{v + 1}º Jogo: {apostas[v]}')
    sleep(1)