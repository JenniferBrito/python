from die import Die
import pygal

# Cria um d6
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
# Cria um histograma
hist = pygal.Bar()

hist.title = 'Resultados de jogar um d6 1000x'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Resultado'
hist.y_title = 'Frequência do resultado'

hist.add('d6', frequencies)
hist.render_to_file('die_visual.svg')