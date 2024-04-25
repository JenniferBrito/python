# ex072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Valor inválido tente novamente.')
    else:
        print('=' * 30)
        print(f'O valor {num} escrito de forma extensa é {extenso[num]}.')
        break
