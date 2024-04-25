# ex073: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. 
# Depois mostre: 
# a - apenas os 5 primeiros colocados, 
# b - os últimos 4 colocados da tabela, 
# c - uma lista com os times em ordem alfabética, 
# d - em que posição está o time da chapecoense

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 
         'Fluminense', 'Atlético-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('='*100)
print(f'A tabela do campeonato brasileiro de 2023 é: {times}')
print('='*100)
print(f'Os cinco primeiros colocados são {times[0:5]}')
print('='*100)
print(f'Os quatro últimos colocados são {times[16:]}')
print('='*100)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*100)

for pos, c in enumerate(times):
    if 'Chapecoense' in c:
        print(f'A Chapecoense está na posição {times[pos]}')

print('A Chapecoense não está na Série A do Campeonato Brasileiro.')