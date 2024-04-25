# ex054: Crie um programa que leia o ano do nascimento de sete pessoas. 
# No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas já são maiores. Maioridade = 21 anos

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nas = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nas
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('A quantidade de pessoas maiores de idade é {}'.format(totmaior))
print('A quantidade de pessoas menores de idade é {}'.format(totmenor))