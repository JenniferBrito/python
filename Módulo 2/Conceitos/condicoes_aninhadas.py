nome = str(input('Qual o seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é muito popular no Brasil')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#ex036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
#ex037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - binário, 2 - octal, 3 - hexadecimal.
#ex038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais
#ex039: Faça um progrma que leia o ano de nascimento de um jovem e informe: de acordo com sua idade: se ele ainda vai se alistar ao serviço militar , se é a hora de se alistar, se já passou do tempo do alistamento. Seu progrma também deverá mostrar o tempo que falta ou que passou do prazo.
#ex040: Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5 reprovado, media entre 5.0 e 6.9 recuperação, média 7.0 ou superior aprovado
#ex041: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e e mostre sua categoria, de acordo com a idade: até 9 anos mirim,até 14 anos infantil, até 19 anos junior, até 20 anos sênior, acima master
#ex042: Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilatero todos os lados iguais, isosceles dois lados iguais, escaleno todos os lados diferentes
#ex043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status de acordo com a tabela: abaixo de 18.5 abaixo do peso, entre 18.5 e 25 peso ideal, 25 até 30 sobrepeso, 30 até 40 obesidade, acima de 40 obesidade mórbida
#ex044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: a vista dinheiro/cheque 10% de desconto, a vista no cartão 5% de desconto, até 2x no cartão preço normal, 3x ou mais no cartão 20% de juros
#ex045: Crie um programa que faça o computador jogar jokenpô com você