# Os dicionários são variáveis compostas que permitem armazenar 
# vários valores em uma mesma estrutura, acessíveis por chaves literais.
# Para declarar um dicionário se utiliza chaves {} ou dict()
# append não funciona nos dicionários

# dados = dict()
# dados = {'nome': 'Pedro', 'idade': 25}

# print(dados['nome'])
# print(dados['idade'])
# dados['sexo'] = 'M'
# print(dados['sexo'])
# del dados['idade']
# print(dados)

# filme = {'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

# print(filme.values())
# print(filme.keys())
# print(filme.items())

# for k, v in filme.items():
#     print(f'O {k} é {v}')

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# for k in pessoas.keys():
#     print(k)

# brasil = []
# estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado)
# brasil.append(estado2)
# print(brasil[1]['sigla'])

brasil = list()
estado = {}

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for  v in e.values():
        print(v, end=' ')
    print()

# ex090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela. Média 7 ou maior: aprovado.
# ex091: Crie um programa onde quatro jogadores joguem um dado d6 e tenham resultados aleatórios. Guarde os resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# ex092: Crie um programa que leia o nome, ano de nascimento e a carteira de trabalhoe cadastre-os (com a idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente além da idade com quantos anos a pessoa vai se aposentar (35 anos de contribuição).
# ex093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitas em cada partida. No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# ex094: Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: a - quantas pessoas foram cadastradas, b - a média de idade do grupo, c - uma lista com todas as mulheres, d - uma lista com todas as pessoas com idade acima da média.
# ex095: Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento do jogador. 999 p/ sair
