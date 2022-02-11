import pandas as pd
dados = pd.read_csv('../data/imoveis_residenciais_tratados.csv', sep = ';')

# Cria as classes que serão utilizadas para filtrar os imóveis pelo número de quartos
# 1 e 2 quartos
# 3 e 4 quartos
# 5 e 6 quartos
# 7 e 8 quartos
classes = [0, 2, 4, 6, 100]

quartos = pd.cut(dados.Quartos, classes)
print(pd.value_counts(quartos))
'''
Imprime:

(0, 2]      11250 # De 1 a 2 quartos
(2, 4]       9681 # De 3 a 4 quartos
(4, 6]        686 # De 5 a 6 quartos
(6, 100]       50 # 7 ou mais quartos
Name: Quartos, dtype: int64

Nesse resultado o ( significa intervalo aberto, ou seja o valor junto ao ( não faz parte do intervalo.
Já o ] indica intervalo fechado e que o valor faz parte do intervalo.
'''

# Colocando lables no resultado
labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais' ]
quartos = pd.cut(dados.Quartos, classes, labels = labels)
print(pd.value_counts(quartos))