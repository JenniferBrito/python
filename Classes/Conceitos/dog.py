# Exemplo de classe retirada do livro Curso Intensivo de Python: Uma introdução prática e baseada em projetos à programação

class Dog():
    """Uma tentativa simples de modelar um cachorro"""

    def __init__(self, name, age):
        """Inicializa os atributos name e age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um comando"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(self.name.title() + ' rolled over!')

my_dog = Dog('Willie', 6)

print("My dog's name is " + my_dog.name.title())
print("My dog's age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()