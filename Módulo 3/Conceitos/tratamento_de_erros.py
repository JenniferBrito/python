try: # operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados informados.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as error: # falha
    print(f'O erro encontrado foi {error.__cause__}')
else: # deu certo
    print(f'O resultado é {r:.1f}')
finally: # algo que vai acontecer sempre independente do resultado
    print('Volte sempre, muito obrigado')

# ex113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma funão leiaFloat() com a mesma funcionalidade.
# ex114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
# ex115: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
