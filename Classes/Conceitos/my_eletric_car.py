"""Importa e cria uma instância da classe EletricCar"""

from car import EletricCar

my_eletric_car = EletricCar('byd', 'dolphin', 2024)

print(my_eletric_car.get_descriptive_name())
my_eletric_car.battery.describe_battery()
my_eletric_car.battery.get_range()

