# ex042: Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
# equilatero todos os lados iguais, isosceles dois lados iguais, escaleno todos os lados diferentes

a = float(input('Entre com o primeiro valor: '))
b = float(input('Entre com o segundo valor: '))
c = float(input('Entre com o terceiro valor: '))

ab = a + b # a + b > c
bc = b + c # b + c > a
ac = a + c # a + c > b

if ab > c and bc > a and ac > b:
    print('As três retas formam um triângulo.')
    if a == b == c:
        print('O triângulo será equilátero.')
    elif a != b != c != a:
        print('O triângulo será escaleno.')
    else:
        print('O triângulo será isósceles.')
else:
    print('As três retas não formam um triângulo.')