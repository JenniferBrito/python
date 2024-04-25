from time import sleep
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver cadastros', 'Novo cadastro', 'Sair do sistema'])
    if resp == 1:
        # opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(2)
