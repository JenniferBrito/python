# ex022: crie um programa que leia um nome completo e mostre o nome com todas as letras maiúsculas, 
# todas minúsculas, letras ao todo (sem espaço), quantas letras no primeiro nome

nome = input('Digite o nome completo: ').strip()

print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Letras ao todo: {}'.format(len(nome) - nome.count(' ')))
# print('Letras ao todo no primeiro nome: {}'.format(len(nome.split()[0])))
print('Letras ao todo no primeiro nome: {}'.format(nome.find(' ')))