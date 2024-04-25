# ex105: Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
#     - quantidade de notas, 
#     - a maior nota, 
#     - a menor nota, 
#     - a média da turma, 
#     - a situação (opcional). 
# Adicione também as docstrings da função


def notas(*bol, sit = False):
    """
    -> Recebe n notas e registra em um dicionário a quantidade de notas, maior e menor nota, média da turma, e situação.
    :param bol: notas inseridas
    :param sit: valor opcional, caso queira ver a situação da turma
    :return: dicionário com as informações desejadas
    """
    boletim = dict()

    # Qtd de notas
    boletim['qtd'] = len(bol)

    # Maior nota
    boletim['maior'] = max(bol)

    # Menor nota
    boletim['menor'] = min(bol)

    # Média da turma
    boletim['media'] = sum(bol) / len(bol)

    # Situação
    if sit:
        if boletim['media'] >= 7:
            boletim['sit'] = 'Boa'
        elif boletim['media'] >= 5:
            boletim['sit'] = 'Razoável'
        else:
            boletim['sit'] = 'Ruim'
    return boletim
    


resp = notas(6, 5, 9, 10, 8.5, sit=True)
print(resp)
help(notas)