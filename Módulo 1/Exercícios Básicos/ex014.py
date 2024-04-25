# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temp = float(input('Digite a temperatura em ºC: '))

f = temp * 9/5 + 32

print('A temperatura {:.1f}ºC corresponde a {:.1f}ºF!'.format(temp, f))