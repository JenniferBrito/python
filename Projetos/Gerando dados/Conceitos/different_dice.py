"""Lança dois dados, d6 e d10 e analisa seus resultados"""

from die import Die
import pygal

# Cria um d6
die_1 = Die()
die_2 = Die(10)

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
# Cria um histograma
hist = pygal.Bar()

hist.title = 'Resultados de jogar um d6 e um d10 50.000x'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
                 '12', '13', '14', '15', '16']
hist.x_title = 'Resultado'
hist.y_title = 'Frequência do resultado'

hist.add('d6 + d10', frequencies)
hist.render_to_file('dice_v2_visual.svg')