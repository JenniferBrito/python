# Tentativas de login: Acrescente um atributo chamado login_attempts à sua
# classe User do Exercício 9.3 (página 226). Escreva um método chamado
# increment_login_attempts() que incremente o valor de login_attempts em 1.
# Escreva outro método chamado reset_login_attempts() que reinicie o valor de
# login_attempts com 0.
# Crie uma instância da classe User e chame increment_login_attempts()
# várias vezes. Exiba o valor de login_attempts para garantir que ele foi
# incrementado de forma apropriada e, em seguida, chame
# reset_login_attempts(). Exiba login_attempts novamente para garantir que
# seu valor foi reiniciado com 0.

class User():
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'Nome completo: {self.first_name} {self.last_name}')
        print(f'Idade: {self.age}')
        print(f'Username: {self.username}')
    
    def greet_user(self):
        print(f'Olá, {self.first_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Pip', 'Fitz-Amobi', 'pipamobi', 17)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f'Tentativas de login: {user1.login_attempts}' )

print('='*30)

user1.reset_login_attempts()
print(f'Tentativas de login: {user1.login_attempts}')