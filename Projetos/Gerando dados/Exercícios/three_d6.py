"""
Se lançar três dados D6, o menor número que você poderá
obter é 3 e o maior número é 18. Crie uma visualização que mostre o que
acontece quando lançamos três dados D6
"""

from die import Die
import pygal

# Cria três d6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
# Cria um histograma
hist = pygal.Bar()

hist.title = 'Resultados de jogar três d6 1000x'

hist.x_labels = [f'{x}' for x in range(3, max_result+1)]
hist.x_title = 'Resultado'
hist.y_title = 'Frequência do resultado'

hist.add('3d6', frequencies)
hist.render_to_file('three_dice.svg')