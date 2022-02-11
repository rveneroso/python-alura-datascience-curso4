import pandas as pd
dados = pd.read_csv('../data/imoveis_residenciais_tratados.csv', sep = ';')

# Cria a variável Valor Bruto
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
#print(dados)

# Cria a variável Valor m2
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)
#print(dados)

# Cria a variável Valor Bruto m2
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)
#print(dados)

# Cria a variável Tipo Agregado onde todos os tipos que contém Casa em seus nomes receberão o valor Casa e os
# demais receberão o valor Apartamento.
tipos_casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
# O método apply permite que seja aplicada uma função a cada registro de um DataFrame. Na linha abaixo
# temos uma função definida pela palavra reservada lambda.
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in tipos_casa else 'Apartamento')
print(dados)