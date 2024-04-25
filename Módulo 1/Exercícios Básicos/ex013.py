# ex013: faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

valor_inicial = float(input('Digite o valor inicial: '))

valor_final = valor_inicial + (valor_inicial * ( 15 / 100))
print('O novo salário será R${:.2f}'.format(valor_final))