# ex034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários > R$ 1250,00, calcule um aumento de 10%. Para os inferiores o aumento é de 15%.

sal = float(input('Digite o valor do salário: R$ '))

if sal >= 1250:
    aumento = sal + (sal * (10 / 100))
else:
    aumento = sal + (sal * (15 / 100))

print('O valor do novo salário será R$ {:.2f}.'.format(aumento))
