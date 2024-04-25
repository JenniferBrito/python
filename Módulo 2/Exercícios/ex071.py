# ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# Considere as cédulas de 50, 20, 10, 1

valor = int(input('Entre com o valor a ser sacado: R$ '))
total = valor
ced = 50
totalCed = 0

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
          print(f'Total de {totalCed} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break