# ex049: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, utilizando o laço for.

num = int(input('Digite o número desejado: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))