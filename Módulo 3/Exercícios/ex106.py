# ex106: Faça um mini sistema que utilize o interaticve help do python. 
# O usuário vai digitar o comando manual e vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs: use cores
from time import sleep

comando = ''
c = ('\033[m' # 0 - sem cores
     '\033[0;30;41,' # 1 - vermelho
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}') 
    help(com)
    sleep(2)

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print('~'*tam)
    print(msg)
    print('~'*tam)
    sleep(1)
    
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
