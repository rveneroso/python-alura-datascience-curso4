import pandas as pd
data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
'''
Imprime:
0     0.50
1      NaN
2      NaN
3     0.52
4     0.54
5      NaN
6      NaN
7     0.59
8     0.60
9      NaN
10    0.70
dtype: float64

'''

# A interpolação abaixo fará com que os valores NaN sejam preenchidos com o último valor válido para aquela
# coluna
s = s.fillna(method = 'ffill')
#print(s)
'''
Imprime:

0     0.50
1     0.50
2     0.50
3     0.52
4     0.54
5     0.54
6     0.54
7     0.59
8     0.60
9     0.60
10    0.70
dtype: float64

'''

# De maneira análoga existe o método bfill que, em vez de iniciar o preenchimento dos valores ausentes do início
# para o fim da Series, faz o preenchimento do fim para o início da Series. Com isso, o valor a ser utilizado
# no preenchimento de valores ausentes é o valor abaixo do que está ausente.
t = pd.Series(data)
t = t.fillna(method='bfill')
#print(t)
'''
Imprime:

0     0.50
1     0.52
2     0.52
3     0.52
4     0.54
5     0.59
6     0.59
7     0.59
8     0.60
9     0.70
10    0.70
dtype: float64
'''

# Para preencher os valores ausentes com a média dos valores não nulos
s1 = pd.Series(data)
s1.fillna(s1.mean(), inplace=True)
#print(s1)
'''
Imprime:

0     0.500
1     0.575
2     0.575
3     0.520
4     0.540
5     0.575
6     0.575
7     0.590
8     0.600
9     0.575
10    0.700
dtype: float64

'''

# O método ffill possui um parâmetro que permite limitar a quantidade de valores ausentes que serão preenchidos.
# O limite se aplica a cada série de NaN encontrados e não à Series como um todo.
s = pd.Series(data)
s = s.fillna(method = 'ffill', limit=1) # Fará o preenchimento de apenas 1 valor ausente
print(s)
'''
Imprime:

0     0.50
1     0.50
2      NaN
3     0.52
4     0.54
5     0.54
6      NaN
7     0.59
8     0.60
9     0.60
10    0.70
dtype: float64

'''