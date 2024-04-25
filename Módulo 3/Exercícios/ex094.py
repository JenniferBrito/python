# ex094: Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
# e todos os dicionários em uma lista. No final mostre: 
#   a - quantas pessoas foram cadastradas, 
#   b - a média de idade do grupo, 
#   c - uma lista com todas as mulheres, 
#   d - uma lista com todas as pessoas com idade acima da média.

cadastro = list()
pessoa = dict()
total = media  = acima_media = total_idades = 0

while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo: ')).upper()[0]
        if pessoa['sexo']  in 'MF':
            break
        print('Entrada inválida, tente novamente.')    
    pessoa['idade'] = int(input('Digite a idade: '))

    cadastro.append(pessoa.copy())
    total += 1
    print()
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Digite apenas S ou N.')
    if resp == 'N':
        break

print('='*45)
print(f'Foram cadastradas {total} pessoas.')

for c in range(0, total):
    total_idades += cadastro[c]['idade']
media =  total_idades / total
print(f'A média total é de {media} anos.')
print()
print('Lista de mulheres cadastradas')
for c in range(0, total):
   if cadastro[c]['sexo'] in 'F':
        print(f'{cadastro[c]["nome"]}')
print()
print('Lista de pessoas com idade acima da média calculada')
for c in range(0, total):
    if cadastro[c]['idade'] > media:
        print(f'{cadastro[c]["nome"]}')