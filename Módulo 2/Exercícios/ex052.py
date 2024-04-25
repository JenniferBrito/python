# ex052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33n', end='')
        tot +=1
    else:
        print('\033[31n', end='')
    print('{}'.format(c))
print('O número {} foi divisível {} vezes'.format(num, tot))
if tot == 2: 
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo')