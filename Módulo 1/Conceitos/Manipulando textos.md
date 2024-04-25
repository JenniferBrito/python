## Manipulando textos

-- Python é case sensitive

frase = 'Curso em Vídeo Python'

## Fatiamento

-- frase[9] = v => apenas o caractere na posição indicada será selecionado
-- frase[9:13] = Víde => apenas os caracteres no itervalo indicado serão selecionados, excluíndo o número à direita 
-- frase[9:21] = Vídeo Python
-- frase[9:21:2] = VdoPto => começa no 9, vai até o 21, contando de 2 em 2
-- frase[:5] = Curso => começa do 0 até o 4
-- frase[15:] = Python => indica o início e vai até o final
-- frase[9::3] = VePh => indica o início, vai até o final, pulando de 3 em 3


## Análise

-- len(frase) => mostra o comprimento da string
-- frase.count('o') => conta a quantidade de caracteres o existem na frase, nesse exemplo retorna 3
-- frase.count('o', 0, 13) => mesmo que o anterior mas dentro do intervalo 0-13
-- frase.find('deo') => encontra a posição do trecho dentro da string 
-- 'Curso' in frase => diz se a sub string existe na string (True/False)

## Transformação

-- frase.replace('Python', 'Android') => substitui a sub string dentro da string
-- frase.upper() => transforma o que é minúsculo em maiúsculo
-- frase.lower() => transforma o que é maiúsculo em minúsculo 
-- frase.capitalize() => transforma apenas a primeira letra da string em maiúscula
-- frase.title() => analisa as palavras dentro da string e capitaliza as primeiras letras em maiúsculas 

frase =    Aprenda Python  

-- frase.strip() => remove espaços desnecessários no início ou final da string
--- variação: frase.rstrip() => remove espaços no à direita da string
--- variação: frase.lstrip() => remove espaços no à esquerda da string

## Divisão

frase = 'Curso em Vídeo Python'

-- frase.split() => divide a string em 4 novas strings, colocadas em uma lista

## Junção
-- '-'.join(frase) => junta as sub strings em uma só com - como separador