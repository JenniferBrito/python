# Restaurante: Crie uma classe chamada Restaurant. O método __init__()
# de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type.
# Crie um método chamado describe_restaurant() que mostre essas duas
# informações, e um método de nome open_restaurant() que exiba uma
# mensagem informando que o restaurante está aberto.
# Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois
# atributos individualmente e, em seguida, chame os dois métodos.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        print(f'O nome do restaurante é {self.restaurant_name}, e sua especialização é comida {self.cuisine_type}')

    def open_restaurant(self):
        print('O restaurante está aberto agora.')

restaurant = Restaurant('Mamma Mia', 'italiana')

print(f'O nome do restaurante é {restaurant.restaurant_name}')
print(f'A especialidade é comida {restaurant.cuisine_type}')
print('-'*30)
restaurant.describe_resturant()
restaurant.cuisine_type