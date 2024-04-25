# ex086: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

# valores = [[], [], []]

# for v in range(0, 3):
#     valores[0].append(int(input(f'Digite o {v + 1}º valor de A: ')))
# print()
# for v in range(0, 3):
#     valores[1].append(int(input(f'Digite o {v + 1}º valor de B: ')))
# print()
# for v in range(0, 3):
#     valores[2].append(int(input(f'Digite o {v + 1}º valor de C: ')))
# print()

# print()
# for v in range(0, 3):
#     print(f'[ {valores[0][v]} ]', end=' ')
# print()
# for v in range(0, 3):
#     print(f'[ {valores[1][v]} ]', end=' ')
# print()
# for v in range(0, 3):
#     print(f'[ {valores[2][v]} ]', end=' ')

# solução da aula

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição[{l}, {c}]: '))

print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()