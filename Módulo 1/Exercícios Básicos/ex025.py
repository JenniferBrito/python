# ex025: crie um progrma que leia o nome de uma pessoa e diga se ela tem o nome 'SILVA'

nome = str(input('Digite o nome da pessoa: ')).strip()

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))