"""
Programa que faz uma chamada API e processa o resultado identificando 
os projetos Python com mais estrelas no GitHub
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena as respostas

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Armazena a resposta da API em uma variável
response_dict = r.json()
print('Total de repositórios: ', response_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']

names, stars = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Cria a visualização

my_style = LS('#333366', base_style= LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_fontsize = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
chart.force_uri_protocol = 'http'
chart.title = 'Projetos no GitHub com mais estrelas'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')