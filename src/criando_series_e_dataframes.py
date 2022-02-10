import pandas as pd

data = [1, 2, 3 , 4, 5] # Cria uma lista

# Para converter a lista acima para uma Series
s = pd.Series(data)

# Criando rótulos para os índices da Series
s = pd.Series(data, index = ['Linha_' + str(i) for i in range(len(data))])

# Também é possível criar o índice a partir de um dicionário.
# Primeiro criamos o dicionário:
dict_indices = {'Linha' + str(i) : i + 1 for i in range(len(data)) }
# Em seguida basta passar o dicionário como parâmetro para o construtor de Series. A Serie criada utilizará
# tanto o índice quanto o valor do dicionário.
s = pd.Series(dict_indices)

# Python aceita operações diretas sobre os valores de uma Series. Por exemplo: a linha abaixo cria uma nova
# Serie na qual o valor dos elementos será o valor original de S acrescido de 2:
s1 = s + 2

# Também é possível realizar operações matemáticas envolvendo duas ou mais Series desde que os índices em todas
# elas sejam os mesmos.
s2 = s + s1
print('Series s')
print('--------')
print(s)
print('\n')
print('Series s1')
print('--------')
print(s1)
print('\n')
print('Series s2')
print('--------')
print(s2)
print('\n')

# Criando um DataFrame a partir de uma lista.
# Cria uma lista contendo 3 listas.
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

df1 = pd.DataFrame(data)

# Criando rótulos para as linhas e colunas do DataFrame
df1 = pd.DataFrame(data, index = ['Linha_' + str(i) for i in range(df1.shape[0])],
                   columns= ['Coluna_' + str(i) for i in range(df1.shape[1])])


# Criando um dicionário para ser usado como fonte do DataFrame
dict_df = {'Coluna_0': {'Linha_0': 1, 'Linha_1': 4, 'Linha_2': 7},
        'Coluna_1': {'Linha_0': 2, 'Linha_1': 5, 'Linha_2': 8},
        'Coluna_2': {'Linha_0': 3, 'Linha_1': 6, 'Linha_2': 9}}

df2 = pd.DataFrame(dict_df)
print(df2)

# Concatenando DataFrames
dados = [(1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)]
df1 = pd.DataFrame(dados, index = ['Linha_' + str(i) for i in range(df1.shape[0])],
                   columns= ['Coluna_' + str(i) for i in range(df1.shape[1])])
df2 = pd.DataFrame(dados, index = ['Linha_' + str(i) for i in range(df1.shape[0])],
                   columns= ['Coluna_' + str(i) for i in range(df1.shape[1])])
df3 = pd.DataFrame(dados, index = ['Linha_' + str(i) for i in range(df1.shape[0])],
                   columns= ['Coluna_' + str(i) for i in range(df1.shape[1])])

# Altera os valores de cada um dos DataFrames criados acima
df1[df1 > 0] = 'A'
df1

df2[df2 > 0] = 'B'
df2

df3[df3 > 0] = 'C'
df3

# Cocatena os 3 DataFrames acima usando as colunas como variáveis de link entre os 3 DataFrames
df4 = pd.concat([df1, df2, df3])
print(df4)

# Agora, concatena os 3 DataFrames usando as linhas como variáveis de link.
df4 = pd.concat([df1, df2, df3], axis=1)
print(df4)