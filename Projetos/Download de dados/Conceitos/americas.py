"""
Mapa simples das Américas
"""

from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Américas do Norte, Central e do Sul'

wm.add('América do Norte', ['ca', 'mx', 'us'])
wm.add('América Central', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('América do Norte', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
       'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
