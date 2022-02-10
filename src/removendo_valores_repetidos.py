import pandas as pd

dados = pd.read_csv('../data/aluguel.csv', sep = ';')
# Trabalhando com uma única variável do DataFrame
tipos_de_imoveis = dados['Tipo'] # Retorna uma variável do tipo <class 'pandas.core.series.Series'>

# Para remover os valores duplicados na Series criada acima. Observação: por default o parâmetro inplace
# tem valor False. Se esse parâmetro não for setado para True, o método drop_duplicates() não surtirá efeito
# na variável sendo alterada. Nesse caso é preciso atribuir o resultado de drop_duplicates() à alguma variável.
tipos_de_imoveis.drop_duplicates(inplace=True)

# Como mencionado acima, tipos_de_imoveis é uma Series. Para transformá-la em um DataFrame:
tipos_de_imoveis = pd.DataFrame(tipos_de_imoveis) # <class 'pandas.core.frame.DataFrame'>

# O DataFrame acima terá os índices correspondentes às linhas utilizadas por ele na remoção de
# duplicidades. Para refazer esses índices tornando-os sequenciais:
tipos_de_imoveis.index = range(tipos_de_imoveis.shape[0])
tipos_de_imoveis.columns.name = 'Id'
print(tipos_de_imoveis)