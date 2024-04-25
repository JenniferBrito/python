# ex040: Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: 
# média abaixo de 5 reprovado, media entre 5.0 e 6.9 recuperação, média 7.0 ou superior aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('A média foi de {:.1f} pontos. Você está reprovado.'.format(media))
elif media >= 5 and media < 7:
    print('A média foi de {:.1f} pontos. Você está de recuperação.'.format(media))
else:
    print('A média foi de {:.1f}. Você está aprovado.'.format(media))
