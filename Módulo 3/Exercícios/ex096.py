# ex096: Faça um programa que tenha uma função chamada área que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l * c
    print(f'A área do terreno {l} x {c} é {area:.2f}m².')

largura = float(input('Digite a largura em metros: '))
comprimento = float(input('Digite o comprimento em metros: '))
area(largura, comprimento)