-- =========================
-- DIMENSÃO DATA
-- =========================
CREATE TABLE dim_data (
    id_data INT PRIMARY KEY,
    data DATE NOT NULL,
    dia INT,
    mes INT,
    trimestre INT,
    ano INT,
    dia_semana VARCHAR(20)
);

-- =========================
-- DIMENSÃO TITULAR
-- =========================
CREATE TABLE dim_titular (
    id_titular INT PRIMARY KEY,
    nome_titular VARCHAR(100),
    final_cartao CHAR(4)
);

-- =========================
-- DIMENSÃO CATEGORIA
-- =========================
CREATE TABLE dim_categoria (
    id_categoria INT PRIMARY KEY,
    nome_categoria VARCHAR(100)
);

-- =========================
-- DIMENSÃO ESTABELECIMENTO
-- =========================
CREATE TABLE dim_estabelecimento (
    id_estabelecimento INT PRIMARY KEY,
    nome_estabelecimento VARCHAR(255)
);

-- =========================
-- TABELA FATO
-- =========================
CREATE TABLE fato_transacao (
    
    id_data INT,
    id_titular INT,
    id_categoria INT,
    id_estabelecimento INT,

    valor_brl DECIMAL(12,2),
    valor_usd DECIMAL(12,2),
    cotacao DECIMAL(10,4),

    parcela_texto VARCHAR(20),
    num_parcela INT,
    total_parcelas INT,

    -- CHAVES ESTRANGEIRAS
    CONSTRAINT fk_data
        FOREIGN KEY (id_data)
        REFERENCES dim_data(id_data),

    CONSTRAINT fk_titular
        FOREIGN KEY (id_titular)
        REFERENCES dim_titular(id_titular),

    CONSTRAINT fk_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES dim_categoria(id_categoria),

    CONSTRAINT fk_estabelecimento
        FOREIGN KEY (id_estabelecimento)
        REFERENCES dim_estabelecimento(id_estabelecimento)
);