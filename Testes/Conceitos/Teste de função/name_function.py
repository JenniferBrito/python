# Testes em Python

# Os testes provam que um código funciona da forma que deve ser.
# Todo programador comete erros e por isso deve testar seus códigos.
# Para aprender a testar precisamos de um código para testes.

# Testando uma função
# def get_formatted_name(first, last):
#     """Gera um nome completo formatado de forma elegante"""
#     full_name = first + ' ' + last
#     return full_name.title()

# A função get_formatted_name combina o primeiro nome e sobrenome informados
# com um espaço entre eles, e converte as primeiras letras em maiúsculas.

# Alterando a função para tratar nomes do meio
# def get_formatted_name(first, middle, last):
#     """Gera um nome completo formatado de forma elegante"""
#     full_name = first + ' ' + ' '+ middle + ' ' + last
#     return full_name.title()

# Corrigindo o erro causado pela exigência do parâmetro middle
def get_formatted_name(first, last, middle=''):
    """Gera um nome completo formatado de forma elegante"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()