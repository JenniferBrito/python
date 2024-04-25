#Break

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma dos valores é {}'.format(s))

#FStrings

print(f'A soma vale {s}')

nome = 'jose'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}')

# ex066: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999m que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando a flag.
# ex067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# ex068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando a quantidade de vitórias consecutivas do jogador.
# ex069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a - quantas pessoas tem mais de 18 anos, b - quantos homens foram cadastrados, c - quantas mulheres tem menos de 20 anos
# ex070: Crie um programa que leia o nome e o preço de vários produtos, o programa deverá perguntar se o usuário vai continuar. no final mostre: a - qual o total gasto na compra, b - quantos produtos custam mais de R$ 1000, c - qual é o nome do produto mais barato
# ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere as cédulas de 50, 20, 10, 1