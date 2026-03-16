import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# CONFIGURAÇÕES
# -----------------------------

# Caminho do arquivo CSV exportado do Excel
CSV_FILE = "data/Fatura_2026-01-20.csv"

# String de conexão do banco (MySQL)
DB_CONNECTION = "mysql+pymysql://usuario:senha@localhost:3306/datawarehouse"

# Nome da tabela destino no Data Warehouse
TABLE_NAME = "fato_vendas"

# -----------------------------
# EXTRACT
# -----------------------------
def extract():
    print("Extraindo dados do CSV...")

    df = pd.read_csv(CSV_FILE, encoding="utf-8", sep=",")

    return df

# -----------------------------
# TRANSFORM
# -----------------------------
def transform(df):
    print("Transformando dados...")

    # Padronizar nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remover linhas totalmente vazias
    df = df.dropna(how="all")

    # Exemplo de conversões
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], errors="coerce")

    if "valor" in df.columns:
        df["valor"] = (
            df["valor"]
            .astype(str)
            .str.replace(",", ".")
            .astype(float)
        )

    # Remover duplicados
    df = df.drop_duplicates()

    return df

# -----------------------------
# LOAD
# -----------------------------
def load(df):
    print("Carregando dados no Data Warehouse...")

    engine = create_engine(DB_CONNECTION)

    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="append",   # append / replace
        index=False
    )

    print("Carga finalizada com sucesso!")

# -----------------------------
# PIPELINE ETL
# -----------------------------
def run_etl():
    df = extract()
    df_transformado = transform(df)
    load(df_transformado)


if __name__ == "__main__":
    run_etl()