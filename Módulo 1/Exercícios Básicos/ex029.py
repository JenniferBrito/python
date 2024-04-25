# ex029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$ 7,00 por cada km acima do limite.

vel = float(input('Entre com a velocidade do carro em km: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('Você está acima dos limites de velocidade, seu carro foi multado. O valor a ser pago é: R$ {:.2f}'.format(multa))
else:
    print('Você está dentro dos limites da velocidade.')