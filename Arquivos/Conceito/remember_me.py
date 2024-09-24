# É conveniente salvar dados gerados pelo usuário com json pois caso elas
# não sejam salvas de algum modo, serão perdidas após o fim do programa.
# Por exemplo:

# import json

# username = input('Qual o seu nome? ')

# filename = 'username.json'

# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print(f'Vamos nos lembrar de você, {username}!')

# Combinando os programas remember_me e greet_user, temos:

# import json

# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

# Refatorando o código para melhor leitura e compreensão

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
         return None
    else:
         return username

def get_new_username():
    username = input('Qual o seu nome? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f'Bem-vinde de volta, {username}!')     
    else:
       get_new_username()
       print(f'Vamos nos lembrar de você, {username}!')

greet_user()