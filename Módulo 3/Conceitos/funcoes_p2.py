# Funções parte 2

# Interactive help
# Mostra o manual do python de forma interativa
# help()
# help(input)
# print(input.__doc__)

# Docstrings
# Manual que é exibido quando solicitado usando a interactive help
# def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela:
#    :param i: início da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    """
#    c = i
#    while c <= f:
#       print(f'{c}', end='..')
#       c += p
#    print('Fim')
# help(contador)
# contador(2, 10, 2)


# Argumentos opcionais
# Atribuição de um valor padrão ao parâmetro
# def somar(a = 0, b = 0, c = 0):
#     s = a + b + c
#     print(f'A soma vale {s}')

# somar(3, 2, 5)
# somar(8, 4)
# somar()

# Escopo de variáveis
# Local onde uma variável existe dentro de um programa 
# Global: a variável vai existir em todo o programa
# Local: vai existir apenas onde foi declarada. Ex: uma função
# Definir uma variável como global faz com que ela seja acessível mesmo fora do escopo local 

# Retorno de resultados

# def somar(a = 0, b = 0, c = 0):
#     s = a + b + c
#     return s

# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = somar(6)
# print(f'Os resultados foram: {r1}, {r2}, {r3}')

def par(n=0):
    if n %2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par')

# ex101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições
# ex102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
# ex103: Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
# ex104: Faça um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante a função input do Python, só que fazendo a validação para aceitar apenas um valor númérico. Ex n = leiaInt('Digite um num: ')
# ex105: Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - quantidade de notas, - a maior nota, - a menor nota, - a média da turma, - a situação (opcional). Adicione também as docstrings da função
# ex106: Faça um mini sistema que utilize o interaticve help do python. O usuário vai digitar o comando manual e vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs: use cores