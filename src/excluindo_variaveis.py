import pandas as pd
dados = pd.read_csv('../data/imoveis_residenciais_tratados.csv', sep = ';')

# Cria a variável Valor Bruto
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']

# Cria a variável Valor m2
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)

# Cria a variável Valor Bruto m2
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)

# Cria a variável Tipo Agregado onde todos os tipos que contém Casa em seus nomes receberão o valor Casa e os
# demais receberão o valor Apartamento.
tipos_casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
# O método apply permite que seja aplicada uma função a cada registro de um DataFrame. Na linha abaixo
# temos uma função definida pela palavra reservada lambda.
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in tipos_casa else 'Apartamento')

# Para excluir variáveis de um DataFrame existem 2 formas diferentes:
# 1- Usando del:
# del dados['Valor Bruto']
# del dados['Valor Bruto m2']

# 2 - Passando a lista de variáveis a serem removidas como argumentos para o método drop. O parâmetro axis = 1
# indica que se deseja remover colunas. Caso se quisesse remover linhas seria necessário fazer axis = 0. Nesse
# exemplo, axis = 0 resultaria em erro já que não temos no DataFrame uma linha com identificadores 'Valor Bruto'
# nem 'Valor Bruto m2'.
dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)

# Exportando a versão final do DataFrame
novos_dados = dados.to_csv('../data/imoveis_residenciais_atualizado.csv', sep = ';', index = False)