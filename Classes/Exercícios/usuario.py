# Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
# first_name e last_name e, então, crie vários outros atributos normalmente
# armazenados em um perfil de usuário. Escreva um método de nome
# describe_user() que apresente um resumo das informações do usuário. Escreva
# outro método chamado greet_user() que mostre uma saudação personalizada ao
# usuário.
# Crie várias instâncias que representem diferentes usuários e chame os dois
# métodos para cada usuário.

class User():
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age

    def describe_user(self):
        print(f'Nome completo: {self.first_name} {self.last_name}')
        print(f'Idade: {self.age}')
        print(f'Username: {self.username}')
    
    def greet_user(self):
        print(f'Olá, {self.first_name}!')


user1 = User('Pip', 'Fitz-Amobi', 'pipamobi', 17)
user2 = User('Ravi', 'Singh', 'ravishing', 20)
user3 = User('Cara', 'Ward', 'caraward', 17)

print('-'*30)
user1.describe_user()
user1.greet_user()

print('-'*30)
user2.describe_user()
user2.greet_user()

print('-'*30)
user3.describe_user()
user3.greet_user()
