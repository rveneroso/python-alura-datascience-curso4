import pandas as pd
dados = pd.read_csv('../data/imoveis_residenciais_tratados.csv', sep = ';')

# Cria um agrupamento por bairro
grupo_bairro = dados.groupby('Bairro') # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# O atributo groups apresenta diversas informações sobre os grupos criados pelo método groupby.
# print(grupo_bairro.groups) # O resultado é extenso demais para ser incluído aqui.

# Iterando no objeto groups. A variável bairro conterá o nome do bairro e a variável dados um DataFrame para
# cada um dos bairros da lista.
# for bairro, dados in grupo_bairro:
#     print(f'O valor médio do aluguel de imóveis residenciais no bairro {bairro} é {dados.Valor.mean().round(2)}')

# Uma maneira de se obter um resultado semelhante, inclusive com a possibilidade de se obter a média também do
# valor do condomínio é a seguinte:
print(grupo_bairro[['Valor', 'Condominio']].mean().round(2))
