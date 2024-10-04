from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Retorna o código de duas letras do Pygal para um determinado país"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # Se o país não for encontrado, retorne none
    return None
