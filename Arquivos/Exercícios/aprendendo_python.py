# 10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de texto e
# escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
# agora. Comece cada linha com a expressão Em Python podemos.... Salve o
# arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios
# deste capítulo. Escreva um programa que leia o arquivo e mostre o que você
# escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez
# percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma
# lista e então trabalhando com ela fora do bloco with.

# Lendo todo o arquivo
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

print('='*30)

# Percorrendo o arquivo com um laço 
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

print('='*30)

# Armazenando as linhas em uma lista e trabalhando com ela fora do bloco with
with open(filename) as file_object:
    lines = file_object.readlines()

learning_string = ''

for line in lines:
    learning_string += line.strip()

print(learning_string)