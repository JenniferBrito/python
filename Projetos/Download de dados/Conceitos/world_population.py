"""
Extraindo dados de um arquivo json
"""

import json
# Importa a função que retorna o código de duas letras de um país
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# Carrega dados em uma lista
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Cria um dicionário com os dados da população
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
    
# Agrupa os países em 3 níveis
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Conta quantos países estão em cada nível
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style = wm_style)
wm.force_uri_protocol ='http'
wm.title = 'População mundial em 2010 por país'
wm.add('0-10M', cc_pops_1)
wm.add('10M-1B', cc_pops_2)
wm.add('>1B', cc_pops_3)

wm.render_to_file('world_population.svg')