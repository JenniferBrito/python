# ex107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilidadesCeV import moeda

n = float(input('Digite o valor: R$ '))

print(f'O dobro de {n} é {moeda.dobro(n):.2f}')
print(f'A metade de {n} é {moeda.metade(n):.2f}')
print(f'Aumentando  em 10%: {moeda.aumentar(n, 10):.2f}')
print(f'Diminuindo em 13%: {moeda.diminuir(n, 13):.2f}')
