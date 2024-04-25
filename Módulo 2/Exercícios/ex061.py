# ex061: Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os primeiros 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
count = 1

while count <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    count += 1

print('Fim')