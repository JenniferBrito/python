# ex041: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e e mostre sua categoria, 
# de acordo com a idade:
# até 9 anos mirim, até 14 anos infantil, até 19 anos junior, até 25 anos sênior, acima master

from datetime import datetime
ano = int(input('Entre com o ano de nascimento: '))

idade = datetime.now().year - ano

if idade <= 9:
    print('A categoria é mirim.')
elif idade <= 14:
    print('A categoria é infantil.')
elif idade <= 19:
    print('A categoria é júnior.')
elif idade <= 25:
    print('A categoria é sênior.')
else:
    print('A categoria é master.')
