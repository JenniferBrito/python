# Convidado: Escreva um programa que pergunte o nome ao usuário.
# Quando ele responder, escreva o nome em um arquivo chamado guest.txt

filename = 'guest.txt'

nome = str(input('Qual o seu nome? '))

with open(filename, 'w') as file_object:
    file_object.write(nome)