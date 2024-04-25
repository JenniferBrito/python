# ex064: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)

num = 0
soma = 0
count = 0

# num = int(input('Digite um número [999 para parar]: '))


while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma = soma + num
        count += 1

print('A soma de {} números digitados é {}.'.format(count, soma))

# Solução do curso
# while num != 999:
#     soma = soma + num
#     count += 1
#     num = int(input('Digite um número [999 para parar]: '))