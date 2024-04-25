# ex069: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre: 
#   a - quantas pessoas tem mais de 18 anos, 
#   b - quantos homens foram cadastrados, 
#   c - quantas mulheres tem menos de 20 anos

maiores = homens = mulheres = 0
resp = ''

while True:
    print('='*30)
    print('Cadastre uma pessoa')
    print('='*30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()

    while sexo not in 'FM':
        sexo = str(input('Digite o sexo [M/F]: ')).upper()
    
        if idade > 18:
            maiores += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
            
    print('='*30)
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp == 'N':
        break

print('='*30)
print(f'A quantidade de pessoas maiores de idade é {maiores}.')
print(f'A quantidade de homens é {homens}.')
print(f'A quantidade de mulheres abaixo de 20 anos é {mulheres}.')