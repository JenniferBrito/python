# ex027: faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente. Ana Maria de Souza, primeiro = Ana, último = Souza

nome = str(input('Digite o nome completo: ')).strip()

print('O primeiro nome é: {}'.format(nome.split()[0]))
print('O último nome é: {}'.format(nome.split()[-1]))