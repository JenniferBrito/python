# ex081: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso mostre: 
# a - quantos números foram digitados, 
# b - a lista de valores ordenados de forma decrescente, 
# c - se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    valores.append(int(input('Digite um número: ')))

    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break

print('=' * 40)
print(f'Foram digitados {len(valores)} valores.')
print('=' * 40)
print('Os valores em ordem decrescente são: ', end='')
valores.sort(reverse=True)

for c in range(len(valores)):
    print(valores[c], end=' ')

print()
print('=' * 40)
if 5 in valores:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')