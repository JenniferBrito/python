# ex011: faça um programa que leia a largura e altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necssária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input('Digite a largura: '))
alt = float (input('Digite a altura: '))

area = larg * alt
tinta = area / 2

print('A área da parede é {}m² e a quantidade de tinta necessária é {}L'.format(area, tinta))
