# ex006: crie um algoritmo que leia um número e mostre o dobro, triplo e raiz quadrada

num = int (input('digite um número: '))

# dobro = num * 2
# triplo = num * 3
# sqrt = num ** 1/2
# sqrt = pow(num, (1/2))

print('o dobro é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}'.format(num*2, num*3, num**(1/2)))