import pandas as pd
dados = pd.read_csv('../data/aluguel.csv', sep = ';')

# Cria a lista de tipos relacionados à imóveis residenciais
residencial = ['Quitinete',
'Casa',
'Apartamento',
'Casa de Condomínio',
'Casa de Vila']

# Verifica, dentre os imóveis presentes no DataFrame, quais são do tipo que pode ser considerado residencial.
# Todos os imóveis estarão presentes no resultodo mas os que não forem residenciais estarão com o valor False.
selecao = dados['Tipo'].isin(residencial)
dados_residencial = dados[selecao]
# Reindexa o DataFrame
dados_residencial.index = range(dados_residencial.shape[0])
# Exporta o DataFrame para um arquivo csv sem exportar os índices.
dados_residencial.to_csv('../data/imoveis_residenciais.csv', sep=';', index=False)


