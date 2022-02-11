import pandas as pd
dados = pd.read_csv('../data/imoveis_residenciais.csv', sep = ';')

# Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = dados['Tipo'] == 'Apartamento'
# Retorna o número de ocorrências de imóveis do tipo Apartamento.
n1 = dados[selecao].shape[0] # São 19532
# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
# Quando a seleção envolve mais de um termo, cada termo tem que ser colocado entre parênteses.
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0] # São 2212
# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0] # São 8719
# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0] # São 41

# Impressão dos resultados.
print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))