# def mostraLinha():
#     print('---------------------------------------------')

# mostraLinha()
# print('     SISTEMA DE ALUNOS       ')
# mostraLinha()
# mostraLinha()
# print('     CADASTRO DE FUNCIONÁRIO     ')
# mostraLinha()
# mostraLinha()
# print('     ERRO DE SISTEMA         ')
# mostraLinha()

# def mensagem(msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)

# mensagem('      SISTEMA DE ALUNOS       ')
# mensagem('      CADASTRO DE FUNCIONÁRIO     ')
# mensagem('      ERRO DE SISTEMA     ')

# def soma(a, b):
#     result = a + b
#     print(result)

# soma(4, 5)
# soma(6, 9)

# def contador(*num):
#     print(f'Recebi os valores {num} e foram {len(num)} números.')    

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(4, 6, 7)

# ex096: Faça um programa que tenha uma função chamada área que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# ex097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex: escreva('Olá mundo!'), saída: ~~~~~~Olá, Mundo!~~~~~~
# ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar 3 contagens através da função criada: a - de 1 até 10, de 1 em 1, b - de 10 até 0, de 2 em 2, c - uma contagem personalizada
# ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos e dizer qual é o maior.
# ex100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre os valores pares sorteados pela função anterior.