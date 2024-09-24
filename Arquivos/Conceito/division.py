# Exceções

# Python utiliza exceções para administrar erros que surgirem durante a
# execução de um programa. Se uma exceção for tratada, o programa 
# continuará sendo executado de forma normal, caso não seja tratada, 
# o programa será interrompido e um traceback, com informações sobre a 
# exceção será exibido.

# Exceções são tratadas com blocos try-except. Esses blocos pedem ao python
# que executem algo, e também diz o que deve ser feito em caso de exceção.

# Exceção ZeroDivisionError

# Um erro simples que retorna uma exceção é a divisão de um número por 0

# print(5/0)

# O erro informado, ZeroDivisionError, é um objeto exceção. Quando existir
# a possibilidade de um erro usamos o bloco try-except.

# try:
#     print(5/0)
# except:
#     print('Não é possível dividir por zero!')

# Se o código no bloco try funcionar, o bloco except será ignorado.
# Se o código no bloco try causar um erro, o interpretador procurará 
# um bloco except que corresponda ao erro causado.

print('Entre com dois números para fazer uma divisão.')
print("Digite 'q' para sair.")

while True:
    first_number = input('\nPrimeiro número: ')
    if first_number == 'q':
        break

    second_number = input('\nSegundo número: ')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Não é possível dividir por 0!")
    else:
        print(answer)

# O bloco else depende da execução sem erros do bloco try.

