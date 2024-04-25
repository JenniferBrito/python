# ex060: Faça um programa que leia um número qualquer e mostre seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# from math import factorial

# n = int(input('Digite um número: '))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))

num = int(input('Digite o número: '))
c = num
fat = 1

print('Calculando {}! = '.format(num), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * c
    c -= 1

print('{}'.format(fat))