# ex039: Faça um progrma que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 
# se ele ainda vai se alistar ao serviço militar , se é a hora de se alistar, se já passou do tempo do alistamento. 
# Seu progrma também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano = int(input('Entre com o ano de nascimento: '))

idade = datetime.now().year - ano

if idade == 18:
    print('Você tem {} anos e deve se alistar.'.format(idade))
elif idade < 18:
    alistar = 18 - idade
    print('Você tem {} anos e deve se alistar em {} ano(s)'.format(idade, alistar))
else:
    alistar = idade - 18
    print('Você tem {} anos e deveria ter se alistado há {} anos.'.format(idade, alistar))