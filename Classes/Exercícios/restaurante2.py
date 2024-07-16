# Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
# instâncias diferentes da classe e chame describe_restaurant() para cada
# instância.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        print(f'O nome do restaurante é {self.restaurant_name}, e sua especialização é comida {self.cuisine_type}')

    def open_restaurant(self):
        print('O restaurante está aberto agora.')

restaurant1 = Restaurant('Mamma Mia', 'italiana')
restaurant2 = Restaurant('El cabron', 'espanhola')
restaurant3 = Restaurant('Eugh', 'inglesa')

print('-'*30)
restaurant1.describe_resturant()
print('-'*30)
restaurant2.describe_resturant()
print('-'*30)
restaurant3.describe_resturant()