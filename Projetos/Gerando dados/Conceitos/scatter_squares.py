"""
Pode ser conveniente plotar e estilizar pontos individuais de acordo com
determinadas características. Para plotar um único ponto, se utiliza a 
função scatter(). Passe o valor do ponto (x, y) que deseja para scatter() 
e o valor será plotado.
"""

# import matplotlib.pyplot as plt

# # Chamando scatter, o argumento s define o tamanho dos pontos
# plt.scatter(2, 4, s = 200)

# # Define o título do gráfico e nomeia os eixos
# plt.title('Números ao quadrado', fontsize = 24)
# plt.xlabel('Valor', fontsize = 14)
# plt.ylabel('Valor ao quadrado', fontsize = 14)
# # Define o tamanho dos rótulos das marcações
# plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# plt.show()

# Plotando uma série de pontos

# import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# # Chamando scatter, o argumento s define o tamanho dos pontos
# plt.scatter(x_values, y_values, s = 100)

# # Define o título do gráfico e nomeia os eixos
# plt.title('Números ao quadrado', fontsize = 24)
# plt.xlabel('Valor', fontsize = 14)
# plt.ylabel('Valor ao quadrado', fontsize = 14)
# # Define o tamanho dos rótulos das marcações
# plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# plt.show()

"""Calculando dados automaticamente"""

""""
Em casos onde existem muitos pontos a serem plotados, escrevê-los 
manualmente pode ser ineficiente. Para plotar 1000 pontos podemos fazer:
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
""" Chamando scatter, o argumento s define o tamanho dos pontos, 
o argumento edgecolor remove os contornos dos pontos,
o argumento c permite definir cores para os pontos
cmap é uma série de cores em um gradiente que varia de uma cor inicial a
uma cor final
"""
plt.scatter(x_values, y_values, c = y_values, cmap= plt.cm.Blues, 
            edgecolor= 'none', s = 40)

# Define o título do gráfico e nomeia os eixos
plt.title('Números ao quadrado', fontsize = 24)
plt.xlabel('Valor', fontsize = 14)
plt.ylabel('Valor ao quadrado', fontsize = 14)
# Define o tamanho dos rótulos das marcações
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.show()

"""
Para salvar automaticamente um gráfico em um arquivo, é possível substituir
plt.show() por plt.savefig():
    plt.savefig('squares_plot.png', bbox_inches = 'tight')
O primeiro argumento é o nome a ser dado ao arquivo, que será salvo no 
mesmo diretório do código. O segundo remove espaços em branco extras.
"""