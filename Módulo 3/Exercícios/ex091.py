# ex091: Crie um programa onde quatro jogadores joguem um dado d6 e tenham resultados aleatórios. 
# Guarde os resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
# minha solução
# dado = {}
# resultado = []
# cont = 0

# for c in range(0, 4):
#     dado['nome'] = f'jogador{cont + 1}'
#     dado['valor'] = randint(1, 6)
#     resultado.append(dado.copy())
#     cont += 1

# print('='*40)
# print(f'{"Valores sorteados":^40}')
# print('='*40)
# for c in range(0, 4):
#     print(f'O {resultado[c]["nome"]} teve o resultado {resultado[c]["valor"]}.')
#     sleep(1)
# print('='*30)
# print()

# resultado_ordenado = sorted(resultado, key= lambda dado: dado['valor'], reverse=True)
# print('='*40)
# print(f'{"Ranking de jogadores":^40}')
# print('='*40)

# for c in range(0, 4):
#     print(f'{c + 1}º LUGAR: {resultado_ordenado[c]["nome"]} com {resultado_ordenado[c]["valor"]}')
#     sleep(1)

# Solução da aula
ranking = {}
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'{k} obeteve o resultado {v}.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print('Ranking de jogadores')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')