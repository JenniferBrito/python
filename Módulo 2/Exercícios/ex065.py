# ex065: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

parar ='S'
count = num = media = soma = maior = menor = 0

while parar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
                menor = num
    parar = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
    
media = soma / count

print('A média entre os números digitados é {:.1f}'.format(media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))