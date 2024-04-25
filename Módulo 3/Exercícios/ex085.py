# ex085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separados os 
# valores pares e ímpares. No final mostre os números pares e ímpares em ordem crescente.

valores = [[], []]


for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º valor: '))

    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()

print(f'Os valores pares são: {valores[0]}', end='')
print()
print(f'Os valores ímpares são: {valores[1]}', end='')
