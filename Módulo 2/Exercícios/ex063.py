# ex063: Escreva um programa que leia um número inteiro n qualquer e mostre na tela os n primeiros elementos de uma sequencia fibonacci. 
# ex:  0 - 1 - 1 - 2 - 3 - 5 - 8

termo = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3

print('\n{} -> {}'.format(t1, t2), end='')

while cont <= termo:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
