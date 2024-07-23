"""Uma classe que pode ser usada para representar um carro"""
class Car():
    """Uma tentativa simples de representar um carro"""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro"""
        self.make = make
        self.model = model
        self.year = year
        """Definindo um valor default para um atributo 
        não é necessário incluir um parâmetro para ele"""
        self.odometer_reading = 0
     
    
    def get_descriptive_name(self):
        """Devolve um nome descritivo formatado de modo elegante"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("Esse carro tem " + str(self.odometer_reading) + " quilômetros rodados.")

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Não é possível reverter o hodômetro!')
    
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro"""
        self.odometer_reading += miles
    
"""Várias classes podem ser armazenadas em um mesmo módulo, embora cada classe
em um módulo deve estar de certa forma relacionada com outra. As classes Battery 
e EletricCar ajudam a representar carros, portanto podem ser adicionadas ao módulo
Car"""
class Battery():
    """Uma tentativa de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size=60):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print(f'Esse carro possui uma bateria de {self.battery_size} kWh.')
    
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer
        com essa bateria"""
        if self.battery_size == 60:
            battery_range = 240
        elif self.battery_size == 85:
            battery_range = 270
        print(f'Esse carro faz aproximadamente {battery_range} quilômetros com bateria totalmente carregada.')

class EletricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai
        Em seguida inicializa os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year)
        """Este atributo está relacionado apenas aos carros elétricos criados"""
        self.battery= Battery()
