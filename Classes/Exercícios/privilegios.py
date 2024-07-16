# Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
# atributo privileges que armazene uma lista de strings conforme descrita no
# Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie uma
# instância de Privileges como um atributo da classe Admin. Crie uma nova
# instância de Admin e use seu método para exibir os privilégios.

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

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
       print(f'Os privilégios de administrador são: ')
       for c in range(0, len(self.privileges)):
           print(self.privileges[c])

class Admin(User):
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges()
   


adm = Admin('Nat', 'da Silva', 'natdasilva', 23)
adm.describe_user()
adm.greet_user()
adm.privileges.show_privileges()