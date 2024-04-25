# ex068: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando a quantidade de vitórias consecutivas do jogador.

from random import randint

vitorias = soma = 0

while True:
    comp = randint(1, 10)
    escolha = str(input('Escolha par ou ímpar: ')).strip().lower()
    jogador = int(input('Digite um número de 1 a 10: '))
    
    soma = jogador + comp
    if soma % 2 == 0:
        result = 'par'
    else:
        result = 'ímpar'
    if escolha == result:
        print('='*30)
        print(f'Você escolheu {escolha} e jogou {jogador}.')
        print(f'O computador jogou {comp}. Total de {soma}')
        print(f'Vitória do jogador. Resultado: {result}')
        print('='*30)
        vitorias += 1
    else:
        print('='*30)
        print(f'Você escolheu {escolha} e jogou {jogador}.')
        print(f'O computador jogou {comp}. Total de {soma}')
        print(f'Vitória do computador. Resultado: {result}')
        print('='*30)
        break

print(f'Jogo encerrado. Você teve {vitorias} vitória(s).')