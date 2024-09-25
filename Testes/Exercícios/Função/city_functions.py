"""
Cidade, país: Escreva uma função que aceite dois parâmetros: o nome de
uma cidade e o nome de um país. A função deve devolver uma única string no
formado Cidade, País, por exemplo, Santiago, Chile. Armazene a função em
um módulo chamado city_functions.py.
Crie um arquivo de nome test_cities.py que teste a função que você acabou de
escrever (lembre-se de que é necessário importar unittest e a função que você
quer testar). Escreva um método chamado test_city_country() para conferir se a
chamada à sua função com valores como 'santiago' e 'chile' resulta na string
correta. Execute test_cities.py e garanta que test_city_country() passe no teste.

"""
# def city_country(city, country):
#     get_city_country = city + ', ' + country
#     return get_city_country.title()

# Alterando a função para receber o parâmetro  população

def city_country(city, country, pop = ''):
    if pop:
        get_city_country = city + ', ' + country + ' - população ' + pop
    else:
        get_city_country = city + ', ' + country
    return get_city_country.title()