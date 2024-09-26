"""
15.1 – Cubos: Um número elevado à terceira potência é chamado de cubo. Faça
a plotagem dos cinco primeiros números elevados ao cubo e, em seguida, dos
primeiros 5.000 números elevados ao cubo.
15.2 – Cubos coloridos: Aplique um colormap ao seu gráfico de cubos.
"""
import matplotlib.pyplot as plt

# 5 primeiros números com colormap

# x_values = list(range(1, 6))
# y_values = [x**3 for x in x_values]

# plt.scatter(x_values, y_values, c = y_values, 
#             cmap = plt.cm.Blues, edgecolors = 'none', s = 45)

# plt.title("Valores ao cubo", fontsize = 24)
# plt.xlabel('Valores', fontsize = 14)
# plt.ylabel('Valores ao cubo', fontsize = 14)
# plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# plt.show()

# 5000 primeiros números

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values,
            cmap = plt.cm.Blues, edgecolors = 'none', s = 45)
plt.title("Valores ao cubo", fontsize = 24)

plt.xlabel('Valores', fontsize = 14)
plt.ylabel('Valores ao cubo', fontsize = 14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()