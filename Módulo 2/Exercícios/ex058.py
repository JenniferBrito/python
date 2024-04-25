# ex058: Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram nescessários para vencer

import random

num = random.randint(0, 10)
palpite = 0
qtdp = 0

while palpite != num:
    palpite = int(input('Digite seu palpite: '))
    if palpite ==  num:
        print('Parabéns, você acertou em {} tentativas.'.format(qtdp))
    if palpite > num:
        print('Menos, tente novamente.')
    if palpite < num:
        print('Mais, tente novamente.')
    qtdp += 1