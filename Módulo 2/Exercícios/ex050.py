# ex050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, 
# se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma dos números pares é: {}'.format(cont, soma))
