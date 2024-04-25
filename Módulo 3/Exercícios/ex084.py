# ex084: Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma listas. 
# No final mostre: 
# a - quantas pessoas foram cadatradas: pode utilizar o len pra contar a quantidade de pessoas
# b - uma lista com as pessoas mais pesadas, 
# c - uma lista com as pessoas mais leves.

pessoas = list()
dados = []
total = 0
maior = menor = i = j = 0
while True:
    dados.append(str(input('Insira o nome: ')))
    dados.append(float(input('Insira o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    
    if total == 1:
        maior = menor = pessoas[0][1]
    else:
        if pessoas[i][1] > maior:
            maior = pessoas[i][1]
        if pessoas[i][1]< menor:
            menor = pessoas[i][1]
    i += 1

    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break

print('=' * 30)
print(f'Foram cadastradas {total} pessoas.')
print('=' * 30)
print(f'O maior peso é {maior} kg e pertence à: ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]}.', end='')
print()
print(f'O menor peso é {menor} kg e pertence à: ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}.', end=' ')
