# Este programa permite que os usuários forneçam um primeiro nome e 
# sobrenome e o vejam de forma completa e formatada.

from name_function import get_formatted_name

print("Digite q para sair.")

while True:
    first = input('Digite o primeiro nome: ')
    if first == 'q':
        break
    last = input('Digite o sobrenome: ')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f'\tNome formatado: {formatted_name}.')

# Podemos perceber que neste caso os nomes estão corretos. Porém, caso 
# a função get_formatted_name() seja modificada para lidar com nomes do 
# meio queremos ter a certeza que erros não acontecerão.
# O módulo unittest da biblioteca padrão python oferece ferramentas de
# teste. Um teste de unidade verifica um aspecto específico do comportamento
# de uma função. Um caso de teste é uma coleção de testes de unidade, prova
# que uma função se comporta como deveria em todas as situações que se espera.
# Um caso de teste com cobertura completa é composto de uma variedade de
# testes de unidade que inclui todas as possíveis maneiras de usar uma função.
# Em geral é suficiente escrever testes para comportamentos críticos do 
# código e então visar uma cobertura completa se o projeto ter seu uso 
# disseminado.


