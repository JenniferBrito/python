# While

# c = 1

# while c < 10:
#     print(c)
#     c += 1

# print('Acabou')

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))

# ex057: FAça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto
# ex058: Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram nescessários para vencer
# ex059: Crie um programa que leia dois valores e mostre um meni na tela: 1 - somar, 2 - multiplicar, 3 - maior, 4 - novos números, 5 - sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
# ex060: Faça um programa que leia um número qualquer e mostre seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# ex061: Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os primeiros 10 primeiros termos da progressão usando a estrutura while.
# ex062: Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
# ex063: Escreva um programa que leia um número inteiro n e qualquer e mostre na tela os n primeiros elementos de uma sequencia fibonacci. ex:  0 -1 1-2-3-5-8
# ex064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos núeros foram digitados e qual foi a soma entre eles (desconsiderando a flag)
# ex065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
