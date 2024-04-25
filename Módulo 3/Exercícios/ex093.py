# ex093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitas em cada partida. 
# No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento = dict()
gols = []
total = 0
aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).strip()
aproveitamento['jogos'] = int(input(f'Quantas partidas {aproveitamento["nome"]} fez? '))

for c in range(0, aproveitamento['jogos']):
   gols.append(int(input(f'Qtd de gols na {c + 1}ª partida: ')))
for c in gols:
   total += c
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = total
print('='*45)
print(f'{aproveitamento["nome"]} fez {aproveitamento["total"]} gols, com distribuição {aproveitamento["gols"]}.')
print('='*45)
print(f'{aproveitamento["nome"]} jogou {aproveitamento["jogos"]} partidas.')
for c in range(0, aproveitamento['jogos']):
    print(f'    => Na partida {c + 1} fez {aproveitamento["gols"][c]} gol(s).')
print(f'Ficando assim com um total de {aproveitamento["total"]} gols na temporada.')