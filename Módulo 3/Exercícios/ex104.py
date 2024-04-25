# ex104: Faça um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante a função input do Python, 
# só que fazendo a validação para aceitar apenas um valor númérico. Ex n = leiaInt('Digite um num: ')

def leiaInt(num):
    ok = False
    valor = 0

    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')