# ex044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# a vista dinheiro/cheque 10% de desconto, a vista no cartão 5% de desconto, até 2x no cartão preço normal, 3x ou mais no cartão 20% de juros

print('Escolha a forma de pagamento:')
print('1 - À vista em dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
pag = int(input('Forma de pagamento: '))
valor = float(input('Entre com o valor a ser pago: '))

if pag == 1:
    total = valor - (valor * (10 / 100))
    print('O valor a ser pago com 10 por cento de desconto é R${:.2f}'.format(total))
elif pag == 2:
    total = valor - (valor * (5 / 100))
    print('O valor a ser pago com 5 por cento de desconto é R${:.2f}'.format(total))
elif pag == 3:
    total = valor / 2
    print('O valor a ser pago em 2x no cartão é R${:.2f}'.format(total))
elif pag == 4:
    total = valor + (valor * (20 / 100))
    parc = int(input('Em quantas parcelas deseja dividir? '))
    tot = total / parc
    print('O valor R${:.2f} a ser pago em {}x no cartão com acréscimo de 20 por cento de juros é R${:.2f}'.format(total, parc, tot))
else:
    print('Escolha uma forma de pagamento válida.')