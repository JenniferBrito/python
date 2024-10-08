"""
Plota três projetos individualmente, com rótulos personalizados
"""

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart= pygal.Bar(style = my_style, x_label_rotation = 45, 
                 show_legend = False)
chart.force_uri_protocol = 'http'
chart.tite = 'Projetos Python'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 1601, 'label': 'Descrição de httpie'},
    {'value': 15028, 'label': 'Descrição de django'},
    {'value': 14798, 'label': 'Descrição de flask'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')