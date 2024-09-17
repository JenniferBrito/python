# Arquivos

# Lendo um arquivo inteiro:
# 
# Para começar criamos um arquivo txt com os valores de pi com 30 casas
# decimais, 10 casas por linha.
# 3.1415926535
# 8979323846
# 2643383279

# Uma forma simples de abrir um arquivo, ler os dados e exibir o conteúdo:

# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents)

# A função open() abre o arquivo, para isso é necessário informar o nome
# do arquivo que se quer abrir. A função devolve um objeto que representa
# o arquivo. Esse objeto será então armazenado em file_object.
# A palavra with fecha o arquivo depois que ele não for mais necessário.
# Pode-se usar close() mas para evitar que um bug não permita que o 
# arquivo seja fehado corretamente, ou que seja chamado de forma precoce 
# se utilizou with.
# O método read() lê todo o conteúdo do arquivo e armazena em uma longa
# string em contents.

# Paths do arquivo 

# Se o arquivo não estiver no mesmo diretório do arquivo .py é preciso
# fornecer o caminho para que o Python possa achá-lo.
# No Linux e OS X o comando seria:
#   with open('text_files/nome_do_arquivo.txt') as file_object:
# No Windows:
#   with open('text_files\nome_do_arquivo.txt') as file_object

# Também é possível dizer o local exato do arquivo no computador, sem se 
# importar com o lugar em que o programa esteja sendo executado no momento. 
# Isso é chamado de path absoluto do arquivo. 
# No Linux e OS X: 
# file_path =
# '/home/ehmatthes/other_files/text_files/nome_do_arquivo.txt'
# with open(file_path) as file_object:

# No Windows:
# file_path =
# 'C:\Users\ehmatthes\other_files\text_files\nome_do_arquivo.txt'
# with open(file_path) as file_object:
# 
# Assim é possível ler arquivos de qualquer lugar do sistema.

# Lendo dados linha a linha
# 
# Podemos usar um laço for no objeto arquivo para analisar cada linha:

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

# filename armazena o path do arquivo facilitando sua utilização em outros 
# momentos do programa e caso haja a necessidade de trocar por outro arquivo.
# O for vai ler cada linha do programa indidualmente e mostrando na tela 
# conforme a leitura acontece juntamente com linhas em branco. Pra remover
# estas linhas brancas, causadas por uma dupla quebra de linha, uma do 
# arquivo e outra da instrução print, usamos o método .rstrip() com o print:
# ficando print(line.rtstrip())


# Lista de linhas em um arquivo

# O objeo devolvido por open() quando utilizamos with ficará apenas no 
# bloco que o contém. Para preservar o acesso ao conteúdo fora deste 
# bloco, é possível armazenar as linhas do arquivo em uma lista dentro
# do bloco e então trabalhar com ela. 
# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# O método readlines() armazena cada linha do arquivo em uma lista. 
# Essa lista é armazenada em lines, com ela é possível trabalhar depois
# do fechamento do bloco with. 

# Depois de ler um arquivo é possível fazer o que quiser com esses dados.
# Primeiro vamos criar uma string contendo todos os dígitos do arquivo,
# sem espaços em branco:

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''

# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

# Primeiro o arquivo é aberto e cada linha é armazenada em uma lista.
# DEpois criamos pi_string para armazenar os dígitos de pi.
# Então um laço que acrescenta cada linha em pi_string removendo a 
# quebra de linha
# Por fim a string e seu tamanho são mostrados.

# IMPORTANTE: todo arquivo texto lido pelo python é interpretado como string.
# Para ler e trabalhar com valores numéricos é necessário convertê-lo para
# int() ou float()

# Os códigos desses exemplos também funcionam em arquivos maiores.
# Criando um arquivo que contenha pi com 1M de casas decimais é possível
# exibir as 50 primeiras casas decimais. Não há nenhum limite inerente de
# quantidade de dados que podem ser trabalhados em python, o limite é a 
# quantidade que a memória do sistema pode tratar.

# filename = 'pi_milion_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''

# for line in lines:
#     pi_string += line.strip()

# print(pi_string[:52]+'...')
# print(len(pi_string))

# Verificando se a data de aniversário contida em pi

filename = 'pi_milion_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Entre com o aniversário, formato mmddyy: ")
if birthday in pi_string:
    print('Seu aniversário está entre o primeiro milhão de dígitos pi!')
else:
    print('Seu aniversário não está entre o primeiro milhão de dígitos de pi!')

