# ex062: Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
count = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1
    print('Pausa')
    mais =int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')