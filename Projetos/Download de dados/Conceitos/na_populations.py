"""
Mapa que mostra as populações dos países da América do Norte
"""

from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Populações dos países da América do Norte'
wm.add('América do Norte', 
       {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
