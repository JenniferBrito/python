# Um teste que passa

# Para escrever um teste é preciso importar o módulo unittest e a função
# a ser testada. 

# Testando a função get_formatted_name

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """Nomes como Janes Joplin funcionam?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_firs_last_middle_name(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 
                                            'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

# Um teste que falha

# Para conseguir um resultado que falha, a função get_formatted_name é 
# modificada para tratar nomes do meio, assim ela gerará um erro para nomes
# que sejam apenas um primeiro nome e sobrenome.
# Quando um teste falha é preciso verificar onde está o erro e corrigí-lo.
# No caso de get_formatted_name, que antes exigia apenas primeiro nome e
# sobrenome, e passou a exigir também um nome do meio, a melhor opção é
# tornar o nome do meio opcional. 