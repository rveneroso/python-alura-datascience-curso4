import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Cria um DataFrame no qual os rótulos das linhas e colunas estarão em ordem decrescente.
df = pd.DataFrame(data, list('321'), list('ZYX'))
print(df)
'''
Imprime:

   Z  Y  X
3  1  2  3
2  4  5  6
1  7  8  9

'''
# Organiza o DataFrame pelo índice das linhas
df.sort_index(inplace=True)
print(df)
'''
Imprime:

   Z  Y  X
1  7  8  9
2  4  5  6
3  1  2  3

'''
# Agora organiza o DataFrame pelo índice das colunas
df.sort_index(inplace=True, axis=1)
print(df)
'''
Imprime:

   X  Y  Z
1  9  8  7
2  6  5  4
3  3  2  1

'''
# Ordena o DataFrame com base nos valores presentes na coluna X
df.sort_values(by = 'X', inplace=True)
print(df)
'''
Imprime:

   X  Y  Z
3  3  2  1
2  6  5  4
1  9  8  7

'''
# Ordena o DataFrame com base nos valores presentes na linha 3
df.sort_values(by = '3', axis = 1, inplace=True)
print(df)
'''
Imprime:

   Z  Y  X
3  1  2  3
2  4  5  6
1  7  8  9

'''
# É possível também ordenar pelos valores de mais de uma coluna.
df.sort_values(by = ['X', 'Y'], inplace=True)
print(df)
'''
Imprime:

   Z  Y  X
3  1  2  3
2  4  5  6
1  7  8  9

'''