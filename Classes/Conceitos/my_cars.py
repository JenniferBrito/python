"""Várias classes podem ser importadas de um mesmo módulo.
Isso pode ser feito separando cada classe com uma vírgula
Para importar o módulo inteiro se usa import {nome do módulo}
É possível importar todas as classes de um módulo utilizando 
from {nome do módulo} import *"""

from car import Car, EletricCar

my_beetle = Car('volkswagen', 'fusca', 2016)
print(my_beetle.get_descriptive_name())

my_eletric_car = EletricCar('byd', 'dolphin', 2024)
print(my_eletric_car.get_descriptive_name())