# ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0
for count in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {count}: ')))

    if count == 0:
        maior = menor = valores[count]
    else:
        if valores[count] > maior:
            maior = valores[count]
        if valores[count] < menor:
            menor = valores[count]


print(f'O maior valor é {maior} e está nas posições ', end='')

for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}, ', end='')
print()
print(f'O menor valor é {menor} e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i},')
print()