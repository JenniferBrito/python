# ex087: Aprimore o desafio anterior, mostrando no final: 
# a - a soma de todos os valores pares digitados, 
# b - a soma dos valores da terceira coluna, 
# c - o maior valor da segunda linha.

valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

total = soma = maior  = 0

for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor para a posição[{l}, {c}]: '))

print()

print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end='')
        if valores[l][c] % 2 == 0:
            total += valores[l][c]
    print()

print()

print(f'A soma de todos os valores pares é {total}.')

print()
# for l in range(0 ,3):
#     soma += valores[l][2]
soma = valores[0][2] + valores[1][2] + valores[2][2]
print(f'A soma dos valores da terceira coluna é {soma}.')

for v in range(0, 3):
    if valores[1][v] > maior:
        maior = valores[1][v]
print()
print(f'O maior valor na segunda linha é {maior}.')