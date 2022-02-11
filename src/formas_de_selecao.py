import pandas as pd
data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
# Cria um DataFrame e rotula as linhas como l1, l2, l3 e l4 e as colunas ocmo c1, c2, c3 e c4.
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
'''
Estrutura do DataFrame:

     c1  c2  c3  c4
l1   1   2   3   4
l2   5   6   7   8
l3   8  10  11  12
l4  13  14  15  16

'''

# Para selecionar apenas os valores presentes na coluna c1
series1 = (df['c1'])
#print(series1)
'''
Imprime:

l1     1
l2     5
l3     8
l4    13
Name: c1, dtype: int64

'''

# Para selecionar valores de mais de uma coluna. Observação: os nomes das colunas não precisam ser informados
# na ordem em que aparecem no DataFrame. Nesse caso o objeto retornado será um DataFrame.
data_frame1 = df[['c3', 'c1']]
#print(data_frame1)
'''
Imprime:

c3  c1
l1   3   1
l2   7   5
l3  11   8
l4  15  13
'''

# Selecionando apenas a segunda e terceira linhas do DataFrame
data_frame2 = df[1:3] # Nunca esquecer que o segundo parâmetro é NÃO INCLUSIVO.
#print(data_frame2)

# Para retornar apenas as colunas c3 e c1 de todas as linhas a partir da linha 1
data_frame3 = df[1:][['c3','c1']]
#print(data_frame3)
'''
Imprime:

 c3  c1
l2   7   5
l3  11   8
l4  15  13

'''

# Para selecionar todas as colunas da linha com o rótulo l3. O objeto retornado é uma Series. Lembrando que
# para utilizar o acesso pelo rótulo é necessário usar .loc
series2 = df.loc['l3']
#print(series2)
'''
Imprime:

c1     8
c2    10
c3    11
c4    12
Name: l3, dtype: int64
'''
# Para selecionar todas as colunas das linhas com os rótulos l3 e l2. O objeto retornado é um DataFrame.
# Lembrando que para utilizar o acesso pelo rótulo é necessário usar .loc
data_frame4 = df.loc[['l3', 'l2']]
#print(data_frame4)
'''
Imprime:

 c1  c2  c3  c4
l3   8  10  11  12
l2   5   6   7   8

'''
# Para selecionar o elemento presente na linha l3, coluna c2. objeto retornado é um DataFrame. O objeto
# retornado depende do dado armazenado na posição especificada. Aqui será um numpy.int64
elemento = df.loc['l3', 'c2']
# print(elemento)

# Realizando a mesma operação acima com iloc (uso de índices numéricos).
elemento = df.iloc[2,1]
# print(elemento)

# Para selecionar um grupo de linhas e colunas específicas. O objeto retornado é um DataFrame.
data_frame5 = df.loc[['l3','l1'], ['c4','c2']]
print(data_frame5)
'''
Imprime:

    c4  c2
l3  12  10
l1   4   2
'''

# Realizando a mesma seleção acima utilizando iloc
data_frame6 = df.iloc[[2,0], [3,1]]
print(data_frame6)