# ex103: Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais:
#  o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador ='<desconhecido>', gols= 0):
    print(f'O jogador {jogador} fez {gols} gol(s) na temporada')
    
nome = str(input('Digite o nome: '))
gols = str(input('Digite a quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
  
