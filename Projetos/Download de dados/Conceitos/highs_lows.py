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
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
# Obetendo as datas e as temperaturas máximas e mínimas do arquivo

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Dados não encontrados')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Faz a plotagem dos dados
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = 'red', alpha =0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor ='blue', alpha = 0.1)

# Formata o gráfico
title = 'Temperaturas máximas e mínimas em 2014\nDeath Valley, CA'
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperatura (Fº)', fontsize = 16)
plt.tick_params(axis='both', which ='major', labelsize = 16)

plt.show()