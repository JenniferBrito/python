# ex110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# import moeda
from utilidadesCeV import moeda # ex111

n = float(input('Digite o valor: R$ '))

moeda.resumo(n, 80, 35)

