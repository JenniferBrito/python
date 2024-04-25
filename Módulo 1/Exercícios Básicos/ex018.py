# ex018: Faça um programa que leia um ângulo qualquer e mostre na tela o sen, cos, tg

from math import sin, cos, tan, radians

num = float(input('Digite um ângulo qualquer: '))

sen = sin(radians(num))
coss = cos(radians(num))
tg = tan(radians(num))

print('O seno é {:.2f}, o cosseno é {:.2f}, a tangente é {:.2f}'
      .format(sen, coss, tg))