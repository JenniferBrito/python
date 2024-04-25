# ex059: Crie um programa que leia dois valores e mostre um menu na tela: 
# 1 - somar, 2 - multiplicar, 3 - maior, 4 - novos números, 5 - sair do programa. 
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
sair = False

while sair == False:
    print('\nCalculadora')
    print('1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - Sair do programa')
    opcao = int(input('\nEntre com a sua opção: '))
    if opcao == 1:
        print('\n{} + {} = {}\n'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('\n{} x {} = {}\n'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {}\n'.format(n1, n2))
        if n2 > n1:
            print('O número {} é maior que {}\n'.format(n2, n1))
        if n1 == n2:
            print('O número {} é igual ao número {}\n'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        sair = True
    else:
        print('Opção inválida, tente novamente.')
print('Fim do programa.')