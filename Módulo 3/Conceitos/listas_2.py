# # Listas Compostas

# dados = ('Pedro', 25)
# pessoas = list()

# pessoas.append(dados[:]) # Cria uma cópia de dados dentro de pessoas
# print(pessoas)

# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

# print(pessoas[0][0])
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

# galera = list()
# dado = list()
# totmaior = totmenor = 0
# for c in range(0 ,3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# # print(galera)
    
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior idade')
#         totmaior += 1
#     else:
#         print(f'{p[0]} é menor de idade')
#         totmenor += 1

# ex084: Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma listas. No final mostre: a - quantas pessoas foram cadatradas, b - uma lista com as pessoas mais pesadas, c - uma lista com as pessoas mais leves.
# ex085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separados os valores pares e ímpares. No final mostre os números pares e ímpares em ordem crescente.
# ex086: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
# ex087: Aprimore o desafio anterior, mostrando no final: a - a soma de todos os valores digitados, b - a soma dos valores da terceira coluna, c - o maior valor da segunda linha.
# ex088: Faça um programa que ajude um jogador da mega sena a criar palpites. O programa deverá perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# ex089: Crie um programa que leia nome e nota de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar a nota individual de cada aluno. Interromper com 999
