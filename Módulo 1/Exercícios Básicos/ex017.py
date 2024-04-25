# ex017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa c² = a² + b² => c = sqrt(a² + b²) => c = sqrt(pow(a, 2) + pow(b, 2))

from math import hypot

co = float(input('Digite o C.O.: '))
ca = float(input('Digite o C.A.: '))

hip = hypot(co, ca)
# c = math.sqrt(pow(co, 2) + pow(ca, 2))
# c = ((co**2) +( ca**2))**(1/2)

print('A hipotenusa é {:.2f}'.format(hip))
# print('A hipotenusa é {:.2f}'.format(c))