# ex030: Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Entre com um número inteiro: '))

if num % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))