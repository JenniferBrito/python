# Exceção FilNotFoundError

# Ao trabalhar com arquivos devemos tratar a possibilidade de um arquivo
# estar ausente. Um arquivo pode estar em outro local, nome escrito de
# forma incorreta ou pode não existir, todas essas possibilidades podem
# ser tratadas com um bloco try-except.

# filename = 'alice.txt'

# with open(filename) as f_obj:
#     contents = f_obj.read()

# O interpretador não poderá ler um arquivo não existente, gerando uma
# exceção, FileNotFoundError.

# filename = 'alice.txt'

# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print(f'Desculpe, o arquivo {filename} não existe.')

# Nesse exemplo o programa não tem mais o que fazer caso o arquivo não exista.

# Analisando textos
# 
# Vamos tentar contar contar o número de palavras em alice.txt.

# filename = 'alice.txt'

# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print(f'Desculpe, o arquivo {filename} não existe.')
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f'O arquivo {filename} possui {num_words} palavras.')

# Trabalhando com vários arquivos

# Vamos passar a parte principal desse programa para uma função, facilitando
# a chamada para diversos livros.

# def count_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         print(f'Desculpe, o arquivo {filename} não existe.')
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f'O arquivo {filename} possui {num_words} palavras.')

# filenames = ['alice.txt', 'siddartha.txt', 'moby_dick.txt', 
#              'little_women.txt']
# for filename in filenames:
#     count_words(filename)

# Como o arquivo siddartha não existe, ele não pode ser analisado, 
# se o erro FileNotFound não fosse tratado, os arquivos moby_dick e 
# litte_women não seriam analisados, pois o programa pararia de executar.

# Nem sempre é necessário exibir ao usuário uma mensagem de erro.
# Utilizando a instrução pass é possível executar um bloco except sem 
# fazer mais nada, ela atua como um marcador. Um lembrete que houve a 
# opção de não fazer nada naquele momento ou de futuramente implementar algo.
# Por exemplo escrever em um arquivo missing_files.txt quais arquivos 
# estão ausentes. O usuário não terá acesso, mas poderemos tratá-los de
# forma adequada.

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f'O arquivo {filename} possui {num_words} palavras.')

filenames = ['alice.txt', 'siddartha.txt', 'moby_dick.txt', 
             'little_women.txt']
for filename in filenames:
    count_words(filename)

