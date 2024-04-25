# ex037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 - binário, 2 - octal, 3 - hexadecimal.

num = int(input('Entre com o número desejado: '))
print('Escolha o tipo de conversão que deseja: 1 - binário, 2 - octal, 3 - hexadecimal')
conv = int(input('Entre com a escolha: '))

if conv == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente com um número entre 1 e 3.')