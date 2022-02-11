import pandas as pd
s = pd.Series(list('asdadeadesdasesda'))

# Imprime apenas uma ocorrência de cada valor.
print(s.unique())

# Imprime a frequência com que cada valor ocorre na Series.
print(s.value_counts())
'''
Imprime:
a    5
d    5
s    4
e    3
dtype: int64
'''
# O DataFrame abaixo contém os dados originais do início do curso.
dados = pd.read_csv('../data/aluguel.csv', sep = ';')
print(dados.Tipo.unique())
print(dados.Tipo.value_counts())