# Lista de convidados: Escreva um laço while que pergunte o nome aos
# usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
# acrescente uma linha que registre a visita do usuário em um arquivo chamado
# guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
# arquivo.

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        nome = str(input('Digite o nome do convidado: '))
        print(f'Seja bem-vindo(a), {nome}!\n')

        file_object.write(nome)
        file_object.write('\n')

        resp = str(input('Deseja continuar? [S/N]: '))
        if resp in 'nN':
            break