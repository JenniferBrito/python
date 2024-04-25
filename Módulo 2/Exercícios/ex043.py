# ex043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status de acordo com a tabela: 
# abaixo de 18.5 abaixo do peso, entre 18.5 e 25 peso ideal, 25 até 30 sobrepeso, 30 até 40 obesidade, acima de 40 obesidade mórbida

peso = float(input('Entre com o peso: '))
altura = float(input('Entre com a altura: '))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print('O IMC é {:.2f}, portanto está abaixo do peso ideal.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O IMC é {:.2f}, portanto, está no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('O IMC é {:.2f}, portanto está na categoria sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40 :
    print('O IMC é {:.2f}, portanto está na categoria obesidade.'.format(imc))
else:
    print('O IMC é {:.2f}, portanto está na categoria obesidade mórbida.'.format(imc))