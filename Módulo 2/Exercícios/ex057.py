# ex057: Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. 
# Caso esteja errado peça a digitação novamente até ter um valor correto

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Entrada não válida. Tente novamente.')

print('Obrigada por digitar novamente. O sexo da pessoa é {}'.format(sexo))