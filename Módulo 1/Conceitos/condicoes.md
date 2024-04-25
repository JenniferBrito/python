## Condições 

-- if carro.esquerda():
    bloco True
   else:
    bloco False

-- Exemplo 1
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
print('--Fim--')

-- Exemplo 2

tempo = int(input('Quantos anos tem seu carro? '))

print('Carro novo' if tempo <=3 else 'Carro velho')
print('--Fim--')