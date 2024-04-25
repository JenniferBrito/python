# ex066: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando a flag.

num = soma = cont = 0

while True:
    num = int(input('Entre com um número [999 para sair]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print('='*40)
print(f'A soma de {cont} números digitados é {soma}')
print('='*40)