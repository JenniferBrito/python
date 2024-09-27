"""Rótulos automáticos: Modifique die.py e dice_visual.py substituindo a lista
que usamos para definir o valor de hist.x_labels por um laço que gere essa lista
automaticamente. Se você se sentir à vontade com as list comprehensions,
experimente substituir os outros laços for em die_visual.py e em dice_visual.py por
comprehensions também"""

from die import Die
import pygal

# Cria um d6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for roll_num in range(1000):
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

hist.title = 'Resultados de jogar dois d6 1000x'

hist.x_labels = [f'{x}' for x in range(2, max_result+1)]
hist.x_title = 'Resultado'
hist.y_title = 'Frequência do resultado'

hist.add('d6 + d6', frequencies)
hist.render_to_file('dice_visual_ex.svg')