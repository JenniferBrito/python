# ex051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
   print('{}'.format(c), end=' -> ')
print('Acabou')