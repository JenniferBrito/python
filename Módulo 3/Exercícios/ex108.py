# ex108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() 
# que consiga mostrar os valores como um valor monetário formatado.


# import moeda
from utilidadesCeV import moeda # ex111

n = float(input('Digite o valor: R$ '))

print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'Aumentando em 10%: {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo em 13%: {moeda.moeda(moeda.diminuir(n, 13))}')
