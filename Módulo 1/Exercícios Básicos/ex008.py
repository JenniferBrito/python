# ex008: escreva um programa que leia um valor em metros e converta em cm e mm

num = float(input('Digite o valor em metros: '))

# cm = num * 100
# mm = num * 1000

print('A medida em cm é: {:.2f} \nA medida em mm é {}'.format(num * 100, num * 1000))