# Armazenando dados

# Muitos programas pedem que o usuário forneça informações, é possível
# armazenar esses dados para que eles possam ser utilizados posteriormente.
# O módulo json permite que esses dados sejam acessados facilmente, não
# apenas em programas python, mas também em outras linguagens.

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# A função json.dump() aceita dois argumentos: um dado para armazenar, e
# um objeto arquivo que pode ser usado para armazear o dado.
# Inicialmente o módulo json é importado e uma lista de números criada.
# Em seguida, o arquivo é aberto em modo de escrita, o que permite ao 
# json que escreva nele. O programa não possui saída, mas é possível 
# abrir o arquivo numbers.json e visualizar os dados armazenados.
