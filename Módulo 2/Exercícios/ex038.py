# ex038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
# o primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')