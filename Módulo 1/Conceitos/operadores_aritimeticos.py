# # + Adição
# 5 + 2 == 7
# # - Subtração
# 5 - 2 == 3
# # * Multiplicação
# 5 * 2 == 10
# # / Divisão
# 5 / 2 == 2.5
# # ** Potência
# 5 ** 2 == 25
# # // Divisão inteira
# 5 // 2 == 2
# # % Resto da divisão (mod)
# 5 % 2 == 1

# # Ordem de precedência
# # -- Parênteses ()
# # -- Potência **
# # -- Multiplicação *, divisão /, divisão inteira //, mod %
# # -- Soma +, subtração -

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

add = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
exp = n1 ** n2
divi = n1 // n2
mod = n1 % n2

# print(add)
# print(sub)
# print(multi)
# print(div)
# print(exp)
# print(divi)
# print(mod)

#print('A soma vale {}'.format(n1+n2))
print('A soma vale {}, \na subtração {}, \na multiplicação {}, \ndivisão {:.3f}, \nexp {}, \ndiv inteira {}, \nmod {}'
      .format(add, sub, multi, div, exp, divi, mod))

# Exercícios

# ex005: faça um programa que leia um número inteiro e mostra seu sucessor e antecessor
# ex006: crie um algoritmo que leia um número e mostre o dobro, triplo e raiz quadrada
# ex007: desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média
# ex008: escreva um programa que leia um valor em metros e converta em cm e mm
# ex009: faça um progrma que leia um número inteiro qualquer e mostre na tela sua tabuada
# ex010: crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar, considere US$ 1,00 = R$ 3,27
# ex011: faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necssária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m²
# ex012: faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
# ex013: faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento