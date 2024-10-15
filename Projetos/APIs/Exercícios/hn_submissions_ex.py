"""
Usando os dados de hn_submissions.py, crie
um gráfico de barras que mostre as discussões mais entusiasmadas do momento no
Hacker News. A altura de cada barra deve corresponder ao número de
comentários que cada artigo submetido tem. O rótulo de cada barra deve incluir o
título do artigo submetido, e cada barra deve atuar como um link para a página de
discussão desse artigo.
"""

import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena o resto
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Processa informações sobre cada artigo submetido
submission_ids = r.json()
titles, submission_dicts = [], []

for submission_id in submission_ids[:30]:
    # Cria uma chamada de API separada para cada artigo
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' +
                    str(submission_id),
        'comments': response_dict.get('descendants', 0),
        
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                          reverse=True)

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
chart.x_labels = titles

chart.add('', submission_dicts)
chart.render_to_file('hn_submissions_ex.svg')