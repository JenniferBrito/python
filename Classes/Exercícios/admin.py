# Admin: Um administrador é um tipo especial de usuário. Escreva uma classe
# chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226),
# ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene
# uma lista de strings como "can add post", "can delete post" "can ban user",
# e assim por diante. Escreva um método chamado show_privileges() que liste o
# conjunto de privilégios de um administrador. Crie uma instância de Admin e chame
# seu método.

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

class Admin(User):
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f'Os privilégios de administrador são: ')
        for c in range(0, len(self.privileges)):
            print(self.privileges[c])


adm = Admin('Nat', 'da Silva', 'natdasilva', 23)
adm.describe_user()
adm.greet_user()
adm.show_privileges()