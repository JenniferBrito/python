# Testando a classe AnonymousSurvey

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a clase AnonymousSurvey"""
    
    def setUp(self):
       """Cria uma pesquisa e um conjunto de respostas a serem usados
       em todos os métodos de teste"""
       question = 'Qual o primeiro idioma que você aprendeu a falar?'
       self.my_survey = AnonymousSurvey(question)
       self.responses = ['Inglês', 'Espanhol', 'Mandarin']
       
    
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada corretamente"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas corretamente"""
        for response in self.responses:
           self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()