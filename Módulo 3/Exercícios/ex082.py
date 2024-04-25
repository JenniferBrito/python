# ex082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso crie duas listas extras que vão conter apenas os valores pares e ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

valores = []
impar = []
par =[]

while True:
    valores.append(int(input('Digite um número: ')))
    print('-'*30)
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break
    print('-'*30)

for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
       
print(f'Os números digitados foram: {valores}')
print('='*30)        
print(f'Os números pares digitados são: {par}')
print('='*30)
print(f'Os números ímpares digitados são: {impar}')