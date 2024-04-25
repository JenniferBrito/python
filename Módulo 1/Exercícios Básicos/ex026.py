# ex026: faça um programa que leia uma frase do teclado e mostre quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez, qual posição ela aparece a última vez

frase = str(input('Digite a sua frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))