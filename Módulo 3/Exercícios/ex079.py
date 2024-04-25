# ex079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro ele não será adicionado. 
# No final serão exibidos todos os valores únicos digitados em ordem crescente.

valores = []

while True:
    # valores.append(int(input('Digite um número: ')))
    n = int(input('Digite um valor: '))
    
    if n not in valores:
        valores.append(n)
    else:
        print('Valor já inserido anteriormente.')

    resp = str(input('\nDeseja continuar? [S/N]: ')).strip()
    if resp in 'nN':
        break

print('-' * 30)
print(f'Os valores digitados foram: ', end='')
valores.sort()
for c in range(len(valores)):
    print(valores[c], end=' ')