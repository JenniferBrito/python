# Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma
# classe chamada IceCreamStand que herde da classe Restaurant escrita no
# Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da
# classe funcionará; basta escolher aquela de que você mais gosta. Adicione um
# atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva
# um método para mostrar esses sabores. Crie uma instância de IceCreamStand e
# chame esse método.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        print(f'O nome do restaurante é {self.restaurant_name}, e sua especialização é {self.cuisine_type}.')

    def open_restaurant(self):
        print('O restaurante está aberto agora.')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'morango', 'flocos']

    def show_flavors(self):
        print(f'Os sabores disponíveis são: ')
        for c in range(0, len(self.flavors)):
            print(self.flavors[c])

stand = IceCreamStand('Sorveluxo', 'sorvetes')
stand.describe_resturant()
stand.open_restaurant()
stand.show_flavors()