"""
Fazendo parse dos cabeçalhos de arquivos CSV
"""

"""
CSV é uma maneira simples de armazenar dados em um arquivo texto. 
Os valores são separados por uma vírgula. Estes arquivos podem ter uma 
leitura complicada para as pessoas, mas facilitam a extração e processamento 
de dados por programadores, agilizando a operação de análise de dados.
O módulo csv padrão de python faz parse das linhas de um arquivo csv e
permite rapidamente a extração de valores desejados.
"""
import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
# Obetendo as temperaturas máximas do arquivo

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

# Faz a plotagem dos dados
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(highs, c = 'red')

# Formata o gráfico

plt.title('Temperaturas máximas, julho de 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperatura (Fº)', fontsize = 16)
plt.tick_params(axis='both', which ='major', labelsize = 16)

plt.show()