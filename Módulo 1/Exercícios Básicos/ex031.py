# ex031: Desenvolva um programa que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.

dist = float(input('Qual a distância da viagem em km? '))

if dist <= 200:
    passagem = dist * 0.5
else:
    passagem = dist * 0.45

# passagem = dist * 0.5 if dist <= 200 else dist * 0.45
print('O preço da passagem para uma viagem de {} km é de R$ {:.2f}.'.format(dist, passagem))

