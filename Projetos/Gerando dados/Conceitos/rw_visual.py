"""Plota todos os pontos do passeio"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos

# rw = RandomWalk()
# rw.fill_walk()

# plt.scatter(rw.x_values, rw.y_values, s = 15)
# plt.show()

# Continua criando novos passeios aleátorios enquanto o programa estiver ativo
# Estilizando os pontos
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(figsize = (10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c = point_numbers, 
                cmap=plt.cm.Blues, edgecolor= 'none', s = 1)
    
    # Enfatiza o primeiro e último pontos
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
    edgecolors='none', s=100)

    
    # Remove os eixos
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Gerar outro passeio? (s/n): ')
    if keep_running == 'n':
        break