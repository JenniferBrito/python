# Este programa lê os dados escritos por number_writer.py no arquivo 
# numbers.json 

import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# A função json.load() carrega as informações de numbers.json e guarda na
# variável numbers, e por fim, a lista de números é exibida.