# ex109: Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# import moeda
from utilidadesCeV import moeda # exercício 111

n = float(input('Digite o valor: R$ '))

print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'Aumentando em 10%: {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo em 13%: {moeda.diminuir(n, 13, True)}')
