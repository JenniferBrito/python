"""Crie uma simulação que mostre o que acontece se você lançar
dois dados de oito lados, 1.000 vezes. Aumente o número de lançamentos
gradualmente até começar a perceber os limites da capacidade de seu sistema."""

from die import Die
import pygal

# Cria dois d8
die_1 = Die(8)
die_2 = Die(8)

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

hist.title = 'Resultados de jogar dois d8 1000x'

hist.x_labels = [f'{x}' for x in range(2, max_result+1)]
hist.x_title = 'Resultado'
hist.y_title = 'Frequência do resultado'

hist.add('d8 + d8', frequencies)
hist.render_to_file('two_d8.svg')