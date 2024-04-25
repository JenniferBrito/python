# ex074: Crie um programa que vai gerar 5 números aleatórios e colocar numa tupla. 
# Depois disso mostre os números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
# maior = 0
# menor = 11
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
   
# for c in range(0, 5):
#     if num[c] > maior:
#         maior = num[c]
#     if num[c] < menor:
#         menor = num[c]

print(f'Os números gerados são: {num}')
print(f'O maior número é {max(num)} e o menor é {min(num)}')