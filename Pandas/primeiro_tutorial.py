# Conteúdo retirado do site: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented

# O alias para a importação do pandas é padronizado como pd
import pandas as pd

# Panda armazena dados em tabelas, para isso é preciso criar um DataFrame.
# Um DataFrame é uma estrutura de dados em duas dimensões que pode armazenar
# dados de diferentes tipos (caracteres, int, float, e mais) em colunas.
# É similar a uma planilha, uma tabela SQL ou o data.frame do R.

# A tabela a seguir armazena dados de passageiros do Titanic.
#  Ela possui 3 colunas: 
#       Name: string com o nome, 
#       Age: números inteiros, 
#       Sex: string com o sexo
df = pd.DataFrame({
    "Name": [
        "Braund, Mr. Owen Harris", 
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"], 
})

print(df)

# Cada coluna em um DataFrame é uma Series. Selecionando apenas a coluna Age:

print(df["Age"])

# Para selecionar apenas uma coluna é preciso usar o nome atribuído entre colchetes []
# É similar a seleção de uma coluna em um dicionário Python baseado na chave
# É possível criar uma Series do zero também

ages = pd.Series([22, 35, 58], name="Age")

print(ages)
# Uma série não tem rótulos nas colunas, por ser apenas uma coluna de um DataFrame.
# Uma série tem rótulos nas linhas.

# É possível descobrir a idade do passageiro mais velho no DataFrame selecionando 
# a coluna Age e utilizando max(). Ou diretamente na série. Ex:
print(df["Age"].max())
print(ages.max())

# Para descobrir estatísticas básicas dos dados numéricos do DataFrame é possível
# utilizar o método describe(). Ele retornará um resumo dos dados numéricos, ignorando colunas de texto

print(df.describe()) 