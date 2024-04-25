# ex089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar a nota individual de cada aluno. 
# Interromper com 999

boletim = []
aluno = []
media = 0

while True:
    aluno.append(str(input('Digite o nome: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    boletim.append(aluno[:])
    aluno.clear()
    print()
    resp = str(input('Deseja continuar? [S/N] '))
    print()
    if resp in 'nN':
        break

print('='*40)
print(f'{"BOLETIM":^40}')
print('='*40)

print(f'{"Nº":<15}{"Nome":<15}{"Média"}')

for c in range(0, len(boletim)):
    print(f'{c:.<15}', end='')
    print(f'{boletim[c][0]:.<15}', end='')
    media = (boletim[c][1] + boletim[c][2]) / 2
    print(f'{media}')

print()  
while True:
    num = int(input('Escolha um aluno para ver a nota individual [999 p/ sair]: '))
    if num == 999:
        break
    else:
        print(f'As notas individuais do aluno(a) {boletim[num][0]} são {boletim[num][1]} e {boletim[num][2]}')
    print()