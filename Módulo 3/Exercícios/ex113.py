# ex113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma funão leiaFloat() com a mesma funcionalidade.

def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido. \033[m')
        else:       
            return n

def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real válido. \033[m')
        else:       
            return n
        
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1}')
print(f'Você digitou o número real: {n2}')