# ex067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('Calculadora de Multiplicação')
print('='*40)
while True: 
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for cont in range (1, 11): 
        mult = num * cont
        print(f'{num} x {cont} = {mult}')
        cont += 1
    print('='*40)
print('='*40)
print('Programa de tabuada encerrado!')
print('='*40)