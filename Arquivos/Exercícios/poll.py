# Enquete sobre programação: Escreva um laço while que pergunte às
# pessoas por que elas gostam de programação. Sempre que alguém fornecer um
# motivo, acrescente-o em um arquivo que armazene todas as respostas.

filename = 'poll.txt'

with open(filename, 'w') as file_object:
    while True:
        poll = str(input('Por que você gosta de programação? '))

        file_object.write(poll)
        file_object.write('\n')

        resp = str(input('Deseja continuar? [S/N]: '))
        if resp in 'nN':
            break