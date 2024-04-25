# ex035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Entre com o primeiro valor: '))
b = float(input('Entre com o segundo valor: '))
c = float(input('Entre com o terceiro valor: '))

ab = a + b # a + b > c
bc = b + c # b + c > a
ac = a + c # a + c > b

if ab > c and bc > a and ac > b:
    print('As três retas formam um triângulo.')
else:
    print('As três retas não formam um triângulo.')