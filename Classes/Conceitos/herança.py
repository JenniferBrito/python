"""
Herança: quando a classe que estiver sendo escrita for a versão especializada de
uma outra classe já criada, pode se usar a herança. Quando uma classe herda de 
outra, ela assume automaticamente os métodos e atributos da classe original, que se
chamará classe-pai e a nova classe é a classe-filha.
A classe-filha é livre para também definir novos atributos e métodos próprios.

A primeira tarefa de uma classe-filha é atribuir valores a todos os atributos da
classe-pai. Para isso o __init__ de uma classe-filha precisa de sua classe-pai.

Como exemplo vamos criar uma classe EletricCar que faz tudo que a classe Car faz.
"""

class Car():
    """Uma tentativa simples de representar um carro"""

    def __init__(self, make, model, year):
        """Inicializa os atributos de descrevem um carro"""
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
    
class Battery():
    """Uma tentativa de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print(f'Esse carro possui uma bateria de {self.battery_size} kWh.')
    
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer
        com essa bateria"""
        if self.battery_size == 70:
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

    # def describe_battery(self):
    #     """Exibe uma frase que descreve a capacidade da bateria
    #     e está associado apenas aos carros elétricos"""
    #     print(f'Esse carro possui uma bateria de {self.battery_size} kWh.')

my_eletric_car = EletricCar('byd', 'dolphin', 2024)
print(my_eletric_car.get_descriptive_name())
my_eletric_car.battery.describe_battery()
my_eletric_car.battery.get_range()

"""
Quando uma classe-filha é criada, a classe-pai deve estar no mesmo arquivo e deve
aparecer anres da classe-filha. O nome da classe-pai deve ser incluído entre parênteses
na definição da classe-filha. O método __init__ em EletricCar aceita as informações 
necessárias para criar uma instância de Car.
A função super() é ajuda o Python a criar conexões entre as classes pai e filha.
Essa linha diz ao Python para chamar o método __init__ da classe pai.
Qualquer método da classe-pai que não se enquadre no que a classe-filha estiver
tentando modelar pode ser sobrescrito. Para isso o método deve ter o mesmo nome
da classe-pai que se deseja sobreescrever. Supondo que a classe Car tenha um 
método chamado fill_gas_tank(), ele não faz sentido para um veículo 100% elétrico,
portanto é possível sobreescrever o método na classe EletricCar. Exemplo:
    def fill_gas_tank():
        print('Esse carro não precisa de um tanque de gasolina!')

Em casos onde uma classe possui uma lista crescente de atributos e métodos, uma
parte da classe pode ser escrita de forma separada. A classe maior pode ser dividida
em classes menores que funcionam em conjunto. Por exemplo, se muitos métodos e atributos
estão sendo adicionados à bateria na classe EletricCar, eles podem ser transferidos
para uma classe chamada Battery, e então podemos usar uma instância de Battery como
atributo da classe EletricCar.
Assim é possível adicionar quantos detalhes necessários à bateria sem poluir a classe
EletricCar.
"""
    