import pandas as pd
dados = pd.read_csv('../data/imoveis_residenciais.csv', sep = ';')

# O método abaixo retorna uma matriz booleana contendo, em cada coluna de cada linha do DataFrame o valor True
# se aquele valor for nulo ou False caso não seja.
matriz_nulos = dados.isnull()
#print(matriz_nulos)

# Existe também o método notnull()
matriz_nulos2 = dados.notnull()
#print(matriz_nulos2)

# Uma forma de se obter um resumo das variáveis que contém valores nulos no DataFrame é através do método info()
#print(dados.info())
'''
Imprime:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22580 entries, 0 to 22579
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Tipo        22580 non-null  object 
 1   Bairro      22580 non-null  object 
 2   Quartos     22580 non-null  int64  
 3   Vagas       22580 non-null  int64  
 4   Suites      22580 non-null  int64  
 5   Area        22580 non-null  int64  
 6   Valor       22571 non-null  float64
 7   Condominio  20765 non-null  float64
 8   IPTU        15795 non-null  float64
dtypes: float64(3), int64(4), object(2)
memory usage: 1.6+ MB
None

'''

# Para listar os registros do DataFrame nos quais a coluna valor é nula
imoveis_valores_nulos = dados[dados['Valor'].isnull()]
print(imoveis_valores_nulos)

# Ṕara remover do DataFrame os registros nos quais a coluna Valor seja nula
dados.dropna(subset = ['Valor'], inplace=True)
print(dados.shape[0]) # Deverá apresentar 22571 (9 linhas a menos que o DataFrame original)

# Selecionando os imóveis que são do tipo Apartamento e que estão com o valor de condomínio nulo. Esses registros
# devem ser eliminados do DataFrame.
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())
# Para remover os registros selecionados acima do nosso DataFrame devemos negar o resultado da seleção.
# A negação da seleção é feita com o operador ~
dados = dados[~selecao]

# Apesar da remoção acima, ainda temos imóveis com o valor do condomínio nulo (que não são apartamentos).
# Existem duas formas diferentes de atribuir o valor 0 às variáveis NaN do nosso DataFrame.
# A primeira é através do método fillna do DataFrame
dados.fillna(0, inplace=True)

# A segunda é passar um dicionário contendo os nomes das variáveis e o valor que elas devem receber caso estejam
# com NaN. A vantagem dessa segunda abordagem é que permite que variáveis diferentes recebam valores distintos.
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})

# Para confirmar que não há mais valores nulos no DataFrame podemos usar novamente o método info()
print(dados.info())

# Salvando o DataFrame tratado.
# Reconstrói o índice do DataFrame após as remoções
dados.index = range(dados.shape[0])
novos_dados = dados.to_csv('../data/imoveis_residenciais_tratados.csv', sep = ';', index = False)