# Tuplas

# Tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
# Não pode ser alterada durante a execução do programa, por isso imutável. Ela pode apenas ser apagada. Ex: del(lanche)
# Pode ser criada com ou sem parenteses

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche)
# print(lanche[2])
# print(lanche[1])
# print(lanche[-2])

# for c in lanche:
#     print(f'Eu vou comer {c}')
# print('Estou satisfeito.')

# for c in range(0, len(lanche)):
#     print(lanche[c])

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(2))
print(c.index(8))
print(c.index(2))
print(c.index(5, 1))

# ex072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# ex073: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: a - apenas os 5 primeiros colocados, b - os últimos 4 colocados da tabela, c - uma lista com os times em ordem alfabética, d - em que posição está o time da chapecoense
# ex074: Crie um programa que vai gerar 5 números aleatórios e colocar numa tupla. Depois disso mostre os números gerados e também indique o menor e o maior valor que estão na tupla
# ex075: Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: a - quantas vezes apareceu o valor 9, b - em que posição foi digitado o primeiro valor 3, c - quais foram os números pares
# ex076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final mostre uma listagem de preços, organizando os dados de forma tabular
# ex077: Crie um programa que tenha uma tupla com várias palavras (sem acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
