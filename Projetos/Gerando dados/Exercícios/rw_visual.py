"""Modifique rw_visual.py substituindo plt.scatter()
por plt.plot(). Para simular o percurso de um grão de pólen na superfície de
uma gota d’água, passe rw.x_values e rw.y_values e inclua um argumento
linewidth. Utilize 5.000 em vez de 50.000 pontos"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(figsize = (10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth = 5)
    
    # Enfatiza o primeiro e último pontos
    plt.plot(0, 0, linewidth = 5)
    plt.plot(rw.x_values[-1], rw.y_values[-1], linewidth = 5)

    plt.show()

    keep_running = input('Gerar outro passeio? (s/n): ')
    if keep_running == 'n':
        break