# ex076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. 
# No final mostre uma listagem de preços, organizando os dados de forma tabular

produtos = ('Borracha', 2.50, 'Caderno', 25, 'Caneta', 5.50, 'Lápis', 3.50)

print('='*40)
print(f'{"Listagem de preços":^40}')
print('='*40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='') 
    else:
        print(f'R${produtos[pos]:>7.2f}')