"""
Quando lançamos dois dados, geralmente somamos os
números para obter o resultado. Crie uma visualização que mostre o que acontece
se você multiplicar esses números em vez de somá-los.
"""
import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []

max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Resultado de d6 * d6 50.000x'
hist.x_labels = [f'{x}' for x in range(1, max_result + 1)]
hist.x_title = 'Resultado'
hist.y_title = 'Frequência'

hist.add('d6 * d6', frequencies)
hist.render_to_file('multiplication.svg')