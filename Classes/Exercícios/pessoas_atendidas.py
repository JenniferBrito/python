# Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
# 225). Acrescente um atributo chamado number_served cujo valor default é 0. Crie
# uma instância chamada restaurant a partir dessa classe. Apresente o número de
# clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o
# novamente.
# Adicione um método chamado set_number_served() que permita definir o
# número de clientes atendidos. Chame esse método com um novo número e mostre o
# valor novamente.
# Acrescente um método chamado increment_number_served() que permita
# incrementar o número de clientes servidos. Chame esse método com qualquer
# número que você quiser e que represente quantos clientes foram atendidos, por
# exemplo, em um dia de funcionamento.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_resturant(self):
        print(f'O nome do restaurante é {self.restaurant_name}, e sua especialização é comida {self.cuisine_type}')
        
    def open_restaurant(self):
        print('O restaurante está aberto agora.')

    def read_served(self):
        print(f'Foram servidos {self.number_served} clientes até agora.')
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, num):
        self.number_served += num        

restaurant = Restaurant('Mamma Mia', 'italiana')

print(f'O nome do restaurante é {restaurant.restaurant_name}')
print(f'A especialidade é comida {restaurant.cuisine_type}')
print('-'*30)
restaurant.describe_resturant()
restaurant.cuisine_type

restaurant.read_served()
# restaurant.number_served = 5
restaurant.set_number_served(2)
restaurant.read_served()

restaurant.increment_number_served(150)
restaurant.read_served()
