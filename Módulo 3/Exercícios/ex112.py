# ex112: Dentro do pacote utilidadesCeV que criamos no desafio 111, 
# temos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
# mas com uma validação de dados para aceitar apenas valores que sejam monetário.

from utilidadesCeV import moeda
from utilidadesCeV import dado

n = dado.leiaDinheiro('Digite o valor: R$ ')

moeda.resumo(n, 80, 35)
