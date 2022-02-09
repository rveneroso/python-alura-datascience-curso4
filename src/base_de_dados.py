import pandas as pd

dados = pd.read_csv('../data/aluguel.csv', sep = ';')
tipos_de_dados = pd.DataFrame(dados.dtypes, columns= ['Tipo de Dado'])
tipos_de_dados.columns.name = 'Variáveis'
print(tipos_de_dados)

# Exibe a quantidade de itens (linhas) e variáveis (colunas) de um DataFrame
print(dados.shape)