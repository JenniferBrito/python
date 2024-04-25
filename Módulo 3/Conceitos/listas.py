# Listas

# Listas são variáveis compostas que permitem armazenar valores em uma mesma estrutura,
# acessíveis por chaves individuais. Utilizam [] para a declaração

# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
# print(lanche)

# lanche[3] = 'picolé'
# print(lanche)

# lanche.append('cookie')
# print(lanche)

# lanche.insert(0, 'cachorro quente')
# print(lanche)


# del lanche[3]
# lanche.pop(3)
# lanche.remove('pizza')
# print(lanche)

# if 'pizza' in lanche:
#     lanche.remove('pizza')

# forma de declarar uma lista
valores = list(range(4, 11))

# print(valores)
# valores.sort()
# print(valores)
# valores.sort(reverse=True)
# print(valores)

# print(len(valores))

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')

# val = list()
# for cont in range(0, 5):
#     val.append(int(input('Digite um valor: ')))

# for c, v in enumerate(val):
#     print(f'Na posição {c} encontrei o valor {v}')

a = [2, 3, 4, 7]
# b = a # não é uma cópia dos valores de a, é uma ligação entre as listas
b = a[:] # essa é a forma correta de criar uma cópia de outra lista
b[2] = 8 
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.
# ex079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente.
# ex080: Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inscrição (sem usar o sort). No final, mostre a lista ordenada na tela.
# ex081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: a - quantos números foram digitados, b - a lista de valores ordenados de forma decrescente, c - se o valor 5 foi digitado e está ou não na lista.
# ex082: Crie um programa que vai ler vários números e colocar em uma lista. DEpois disso crie duas listas extras que vão conter apenas os valores pares e ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
# ex083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.