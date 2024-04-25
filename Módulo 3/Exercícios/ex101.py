# ex101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições


def voto(nascimento = 0):
    from datetime import datetime

    idade = datetime.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos NÃO VOTA'
    elif idade == 16 or idade == 17 or idade >= 65:
        return f'Aos {idade} anos o voto é OPCIONAL'
    else:
        return f'Aos {idade} anos o voto é OBRIGATÓRIO'
    
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))