# Testando uma classe 

# Métodos de asserção disponíveis no módulo unittest
"""
assertEqual(a, b) = verifica se a == b
assertNotEqual(a, b) = verifica se a != b
assertTrue(x) = verifica se x é True
assertFalse(x) = verifica se x é False
assertIn(item, lista) = verifica se item está em lista
assertNotIn(item, lista) = verifica se item não está na lista
"""

# Criando uma classe para testar

class AnonymousSurvey():
    """Coleta respostas anônimas para uma pesquisa"""
    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar as respostas"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Mostra a pergunta da pesquisa"""
        print(self.question)

    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa"""
        self.responses.append(new_response)

    def show_results(self):
        """Mostra as respostas dadas"""
        print("Resultado da pesquisa:")
        for response in self.responses:
            print(f'- {response}') 