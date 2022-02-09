import pandas as pd

arquivo_json = open('../data/json/large_json_file.json')

# Criando um DataFrame a partir de um arquivo Json
df_json = pd.read_json(arquivo_json)
print(df_json)

# Criando um DataFrame a partir de um arquivo txt
df_txt = pd.read_table('../data/txt/large_txt_file.txt')
print(df_txt)

# Criando um DataFrame a partir de um arquivo xlsx
df_xslx = pd.read_excel('../data/xlsx/large_xlsx_file.xlsx')
print(df_xslx)

#Criando um DataFrame a partir de uma tabela existente em uma página html
df_html = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')
# A página acima contém 3 tabelas que resultam em 3 dataframes diferentes.
print('Primeiro DataFrame')
print(df_html[0])
print('-------------------')
print('Segundo DataFrame')
print(df_html[1])
print('-------------------')
print('Terceiro DataFrame')
print(df_html[2])
print('-------------------')