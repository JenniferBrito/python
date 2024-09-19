# Escrevendo dados em um arquivo
# Para escrever em um arquivo, chame open() com um segundo argumento 
# indicando que você quer escrever algo.

# Escrevendo em um arquivo vazio
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('Eu amo programar.')

# O primeiro argumento indica o nome do arquivo a ser aberto, 
# o segundo, 'w', indica que queremos abrir em modo de escrita.
# Para modo de leitura: 'r'; modo de escrita: 'w'; modo de concatenação: 'a';
# modo de leitura e escrita: 'r+'

# A função open() cria automaticamente o arquivo caso ele ainda não exista.
# No entanto, se um arquivo já existente for aberto em modo de escrita,
# ele será apagado antes de devolver o objeto arquivo.

# Python escreve apenas strings em um arquivo texto. Se quiser armazenar
# dados númericos é necessário convertê-los antes usando a função str()

# Escrevendo várias linhas

# É necessário inserir uma quebra de linha (\n) para que cada string 
# tenha a sua própria. Também é possível utilizar espaços, tabulação, 
# e linhas em branco para formatar a saída, da mesma forma que fazemos
# no terminal.
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('Eu amo programar.\n')
#     file_object.write('Eu amo criar novos jogos.\n')

# Concatenando dados

# Para acrescentar dados em um arquivo em vez se sobrescrever o conteúdo
# existente, o arquivo deve ser aberto em modo de concatenação. Assim, 
# o python não apagará o arquivo antes de devolver o objeto arquivo.
# Qualquer linha escrita será adicionada ao final. Se o arquivo não existe
# ele será criado.
# Ao final teremos o arquivo original seguido do novo conteúdo.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('Eu amo encontrar sentido em grandes quantidades de dados.\n')
    file_object.write('Eu amo criar apps que funcionam em navegadores.\n')