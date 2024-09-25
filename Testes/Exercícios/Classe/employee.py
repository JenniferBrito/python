"""
Funcionário: Escreva uma classe chamada Employee. O método
__init__() deve aceitar um primeiro nome, um sobrenome e um salário anual, e
deve armazenar cada uma dessas informações como atributos. Escreva um método
de nome give_raise() que some cinco mil dólares ao salário anual, por default,
mas que também aceite um valor diferente de aumento.
Escreva um caso de teste para Employee. Crie dois métodos de teste,
test_give_default_raise() e test_give_custom_raise(). Use o método
setUp() para que não seja necessário criar uma nova instância de funcionário em
cada método de teste. Execute seu caso de teste e certifique-se de que os dois
testes passem.
"""

class Employee():
    """Descreve o funcionário"""
    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
    
    def give_raise(self, salary_raise = 5000):
        """Dá aumento ao funcionário"""
        self.salary += salary_raise
