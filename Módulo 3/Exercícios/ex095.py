# ex095: Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento do jogador. 
# 999 p/ sair

aproveitamento = dict()
gols = []
jogadores = []
total = 0

while True:
    aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).strip()
    aproveitamento['jogos'] = int(input(f'Quantas partidas {aproveitamento["nome"]} fez? '))

    for c in range(0, aproveitamento['jogos']):
        gols.append(int(input(f'Qtd de gols na {c + 1}ª partida: ')))
    for c in gols:
      total += c
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = total
    jogadores.append(aproveitamento.copy())
    gols.clear()    

    print()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break
    else:
        total = 0
    print()

print('='*40)
print(f'{"Lista de jogadores":^40}')
print('='*40)
print(f'{"Nº":<15}{"Nome":<15}')

for c in range(0, len(jogadores)):
    print(f'{c:.<15}', end='')
    print(f'{jogadores[c]["nome"]}', end='')
    print()

while True: 
    jog = int(input(f'Digite o número do jogador para visualizar seu aproveitamento [999 p/ sair]: '))
    
    if jog == 999:
        break
    else:
        print('='*45)
        print(f'{jogadores[jog]["nome"]} fez {jogadores[jog]["total"]} gols, com distribuição {jogadores[jog]["gols"]}.')
        print('='*45)
        print(f'{jogadores[jog]["nome"]} jogou {jogadores[jog]["jogos"]} partidas.')
        for c in range(0, jogadores[jog]['jogos']):
            print(f'    => Na partida {c + 1} fez {jogadores[jog]["gols"][c]} gol(s).')
        print(f'Ficando assim com um total de {jogadores[jog]["total"]} gols na temporada.')