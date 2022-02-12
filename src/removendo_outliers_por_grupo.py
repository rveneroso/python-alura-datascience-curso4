import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_csv('../data/imoveis_residenciais_tratados.csv', sep = ';')

# Cria uma SeriesGroupBy contendo o valor agrupada por tipo de imóvel
grupo_tipo = dados.groupby('Tipo')['Valor']

# Obtendo o primeiro quartil de todos os valores da Serie valor considerando 25%
Q1 = grupo_tipo.quantile(.25) # É do tipo <class 'numpy.float64'>
# Obtendo o terceiro quartil considerando 75%
Q3 = grupo_tipo.quantile(.75)
# Calculando o intervalo inter quartil
IIQ = Q3 - Q1
# Calculando o limite inferior
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
# Selecionando os valores que interessam (desprezando os outliers)
dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])
# Mostrando o histograma dos dados antes e depois da eliminação dos outliers
# dados.hist(['Valor'])
# dados_new.hist(['Valor'])
# Gerando o gráfico
dados_new.boxplot(['Valor'], by = ['Tipo'])
plt.show()
# Salvando o novo DataFrame em um arquivo csv
dados_new.to_csv('../data/aluguel_residencial_sem_outliers_por_tipo.csv', sep = ';', index = False)
