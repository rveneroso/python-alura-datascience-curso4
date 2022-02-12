import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_csv('../data/imoveis_residenciais_tratados.csv', sep = ';')

# Criando uma Series baseada no valor
valor = dados['Valor']

# Obtendo o primeiro quartil de todos os valores da Serie valor considerando 25%
Q1 = valor.quantile(.25) # É do tipo <class 'numpy.float64'>
# Obtendo o terceiro quartil considerando 75%
Q3 = valor.quantile(.75)
# Calculando o intervalo inter quartil
IIQ = Q3 - Q1
# Calculando o limite inferior
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
# Selecionando os valores que interessam (desprezando os outliers)
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
# Cria um novo DataFrame
dados_new = dados[selecao]
# Mostrando o histograma dos dados antes e depois da eliminação dos outliers
dados.hist(['Valor'])
dados_new.hist(['Valor'])
# Gerando o gráfico
#dados_new.boxplot(['Valor'])
plt.show()
