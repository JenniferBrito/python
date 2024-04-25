# ex114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    resp = urllib.request.urlopen('http://www.youtube.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print(f'\033[32mO site Pudim foi acessado com sucesso. \033[m')
    print(resp.read())