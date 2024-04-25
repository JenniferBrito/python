# ex036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Em quantos anos pretende pagar? '))

prestacao = casa / (anos * 12)
porcentagem = salario * (30 / 100)


if porcentagem <= prestacao:
    print('Empréstimo aprovado, prestações mensais de R${:.2f} por {} anos.'.format(prestacao, anos))
elif prestacao < porcentagem:
    print('Empréstimo aprovado, prestações mensais de R${:.2f} por {} anos.'.format(prestacao, anos))
else:
    print('Empréstimo negado, o valor da prestação de R${:.2f} está acima do limite de 30 por cento do salário, que é R${:.2f}'.format(prestacao, porcentagem))