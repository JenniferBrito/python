# ex092: Crie um programa que leia o nome, ano de nascimento e a carteira de trabalho e cadastre-os (com a idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição).

from datetime import datetime

cadastro = dict()

cadastro['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input('Digite o nº da CTPS [0 se não houver]: '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite o valor do salário: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['contratacao'] + 35) - datetime.now().year

print('='*40)
if cadastro['ctps'] != 0:
    print(f'{cadastro["nome"]} tem {cadastro["idade"]} anos, sua CTPS é de nº {cadastro["ctps"]}, ', end='')
    print(f'sua contratação foi em {cadastro["contratacao"]}, seu salário é de {cadastro["salario"]}, ', end='')
    print(f'e vai se aposentar com {cadastro["aposentadoria"]} anos.')
else:
    print(f'{cadastro["nome"]} tem {cadastro["idade"]} anos, não possui CTPS, portanto não tem contribuição ao INSS.')
