# Programa que utiliza a classe AnonymousSurvey

from survey import AnonymousSurvey

# Define uam pergunta e cria uma pesquisa
question = 'Qual idioma você aprendeu a falar primeiro? '
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas à pergunta
my_survey.show_question()
print('Digite q para sair.\n')

while True:
    response = input('Idioma: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa
print('\nObrigada a todos que participaram da pesquisa!')
my_survey.show_results()