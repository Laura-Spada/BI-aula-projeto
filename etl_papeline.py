import pandas as pd
import glob
from sqlalchemy import create_engine

#df_faturas = pd.read_csv("data/Fatura_2026-01-20.csv")

# IMPORTANDO OS ARQUIVOS CSV

arquivos = glob.glob("data/*.csv")

dfs = [pd.read_csv(arquivo, sep=';') for arquivo in arquivos]

df_faturas = pd.concat(dfs)

# print(df_faturas)

# Ordenar os dados pela Categoria
#print(df_faturas.sort_values(by='Categoria', ascending=True))

# Mostrar a quantidade de cada Categoria
#print(df_faturas['Categoria'].value_counts())

# Mostrar a quantidade transações por usuário
#print(df_faturas['Nome no Cartão'].value_counts())

# Mostrar a quantidade de transações por data
#print(df_faturas['Data de Compra'].value_counts())

# CRIANDO NOVO ARQUIVO CSV
"""
colunas = [
    'Data de Compra',
    'Nome no Cartão',
    'Final do Cartão',
    'Categoria',
    'Descrição',
    'Parcela',
    'Valor (em R$)'
]

faturas_df = df_faturas[colunas]

faturas_df.to_csv("data/faturas-2026.csv", index=False)

print("Arquivo criado com sucesso!")
"""

# CRIANDO A TABELA NO SQLITE
engine = create_engine("sqlite:///faturas-2026.db")

"""
df = pd.read_csv("data/faturas-2026.csv")
# print(df)

try:
    df.to_sql('faturas-2026', con=engine, if_exists='replace', index=False)
    print("Sucesso! Dados exportados para a tabela faturas-2026 :)")
except Exception as e:
    print(f"Ocorreu algum erro ao exportar os dados :( {e}")    
"""
    
# CONSULTAS NO SQL
# Total de transações por categoria
consulta_1 = " SELECT Categoria, count('Data de Compra') AS qtd_cat FROM 'faturas-2026' GROUP BY Categoria "
resultado_1 = pd.read_sql_query(consulta_1, engine)
print(resultado_1)

# Total de transações por usuário
consulta_2 = """ SELECT "Nome no Cartão", count(*) AS qtd_trans_user FROM 'faturas-2026' GROUP BY "Nome no Cartão" """
resultado_2 = pd.read_sql_query(consulta_2, engine)
print(resultado_2)

# Total de parcelas únicas
consulta_3 =""" SELECT Parcela, COUNT(*) AS qtd_unicas FROM 'faturas-2026' WHERE Parcela = 'Única' GROUP BY Parcela """
resultado_3 = pd.read_sql_query(consulta_3, engine)
print(resultado_3)

# Total de parcelas únicas por usuário
consulta_3 =""" SELECT "Nome no Cartão", COUNT(*) AS qtd_unicas FROM 'faturas-2026' WHERE Parcela = 'Única' GROUP BY "Nome no Cartão" """
resultado_3 = pd.read_sql_query(consulta_3, engine)
print(resultado_3)

