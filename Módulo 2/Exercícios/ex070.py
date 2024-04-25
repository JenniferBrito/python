# ex070: Crie um programa que leia o nome e o preço de vários produtos, 
# o programa deverá perguntar se o usuário vai continuar. 
# no final mostre: 
#   a - qual o total gasto na compra, 
#   b - quantos produtos custam mais de R$ 1000, 
#   c - qual é o nome do produto mais barato

valorTotal = qtdProduto = menor = cont = 0
maisBarato = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))

    cont += 1

    valorTotal += preco

    if preco >= 1000:
        qtdProduto += 1

    if cont == 1 or preco < menor: 
        menor = preco
        maisBarato = nome
    
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break
    
print('='*30)
print(f'O valor total da compra é R$ {valorTotal:.2f}')
print(f'O total de produtos que custam acima de R$ 1000 é {qtdProduto}')
print(f'O produto mais barato é {maisBarato} custando {menor}')
