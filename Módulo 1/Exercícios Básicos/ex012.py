# ex012: faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco_inicial = float(input('Digite o preço inicial: '))

preco_final = preco_inicial - (preco_inicial * ( 5 / 100))
print('O produto com desconto será R${:.2f}'.format(preco_final))