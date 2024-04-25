# ex010: crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dólares ela pode comprar, considere US$ 1,00 = R$ 3,27 // ajustado para US$ 1,00 = R$ 4,92 em 05/12/23

valor = float(input('Digite o valor em carteira: R$'))

conv = valor / 4.92

print('O valor R${:.2f} convertido passa a US${:.2f}'.format(valor, conv))