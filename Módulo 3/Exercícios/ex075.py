# ex075: Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final mostre: 
# a - quantas vezes apareceu o valor 9, 
# b - em que posição foi digitado o primeiro valor 3, 
# c - quais foram os números pares


num = (int(input('Digite um número: ')), 
       int(input('Digite um número: ')), 
       int(input('Digite um número: ')), 
       int(input('Digite um número: ')))

print(f'Os valores digitados foram {num}.')

print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1} pela primeira vez.')
else:
    print('O valor 3 não foi digitado.')

print('Os números pares são: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')