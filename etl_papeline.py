import pandas as pd
import glob

#df_faturas = pd.read_csv("data/Fatura_2026-01-20.csv")

arquivos = glob.glob("data/*.csv")

dfs = [pd.read_csv(arquivo) for arquivo in arquivos]

df_faturas = pd.concat(dfs)

#print(df_faturas)

# Ordenar os dados pela Categoria
print(df_faturas.sort_values(by='Categoria', ascending=True))

# Mostrar a quantidade de cada Categoria
print(df_faturas['Categoria'].value_counts())

# Mostrar a quantidade transações por usuário
print(df_faturas['Nome no Cartão'].value_counts())

# Mostrar a quantidade de transações por data
print(df_faturas['Data de Compra'].value_counts())
