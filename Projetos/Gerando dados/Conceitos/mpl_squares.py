# Gerando um gráfico linear simples

"""
Vamos gerar um gráfico linear simples usando o matplotlib e depois
personalizá-lo.
Usaremos a sequência 1, 4, 9, 16, 25 de números elevados ao quadrado como 
dados para o gráfico.
"""
# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)
# plt.show()

""" 
O gráfico mostra o que desejamos, mas a letra do rótulo é muito pequena e
a linha muito fina. Com o matplotlib é possível ajustar esses recursos.
"""

# plt.plot(squares, linewidth = 5)

# # Define o título do gráfico e nomeia os eixos
# plt.title("Números elevados ao quadrado", fontsize = 14)
# plt.xlabel("Valor", fontsize = 14)
# plt.ylabel("Valor ao quadrado", fontsize = 14)

# # Define o tamanho dos rótulos das marcações
# plt.tick_params(axis = 'both', labelsize = 14)

# plt.show()

""""
É possível ver que os dados do gráfico não estão plotados corretamente.
Quando uma sequência de números é fornecida a plot(), ele supõe que 
o primeiro ponto de dado corresponde a um valor de coordenada x = 0, mas
neste caso o primeiro ponto corresponde a x = 1. Podemos corrigir isso 
fornecendo ao plot() valores tanto de entrada como de saída usados para 
calcular os quadrados. Dessa forma temos:
"""
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

# Define o título do gráfico e nomeia os eixos
plt.title("Números elevados ao quadrado", fontsize = 14)
plt.xlabel("Valor", fontsize = 14)
plt.ylabel("Valor ao quadrado", fontsize = 14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()

"""
Agora plot() plotará o gráfico corretamente, pois tanto os valores de
entrada quanto de saída foram fornecidos.
"""