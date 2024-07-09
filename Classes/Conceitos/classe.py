# Classes em Python

# Exemplo 01:
# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#          return 'hello world'
#     def __init__(self):
#          self.data = []
    
# x = MyClass()


# Exemplo 02:
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)
# print(x.r, x.i)

# Método __init__
"""
    É um método do Python que executa automaticamente sempre que uma nova instância
    baseada na classe é criada. Tem dois underscores(_) no início e dois no final, 
    evitando que nomes default de métodos Python entrem em conflito com nomes de métodos criados.
    __init__ possui um parâmetro obrigatório, self, que deve estar antes dos demais parâmetros,
    ele dá acesso aos atributos e métodos da classe à instância individual. Qualquer
    variável prefixada com self está disponível a todos os métodos da classe.
"""