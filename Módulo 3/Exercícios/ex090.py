# ex090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final mostre o conteúdo da estrutura na tela. Média 7 ou maior: aprovado.

boletim = dict()

boletim['nome'] = str(input('Digite o nome do aluno: '))
boletim['media'] = float(input(f'Digite a média de {boletim["nome"]}: '))
if boletim['media'] >= 7.0:
    boletim['situacao'] = 'APROVADO(A)'
elif 5 <= boletim['media'] < 7:
    boletim['situacao'] = 'RECUPERAÇÃO'
else:
    boletim['situacao'] = 'REPROVADO(A)'

print(f'Nome do aluno(a): {boletim["nome"]}')
print(f'A média é {boletim["media"]}')
print(f'A situação é {boletim["situacao"]}')