# Neste programa vamos saudar um usuário que já tenha seu nome armazenado

import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print(f'Bem-vinde novamente, {username}')