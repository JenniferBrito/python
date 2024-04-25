# ex077: Crie um programa que tenha uma tupla com várias palavras (sem acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('agua', 'carro', 'bicicleta', 'gato', 'cachorro', 'vaca')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')