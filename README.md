## Modelo Conceitual

<img width="500" height="250" alt="Image" src="assets/conceitual.png" />

## Modelo Lógico

<img width="500" height="250" alt="Image" src="assets/logico.png" />

## SQL

```

CREATE DATABASE Cartaoaula;

CREATE TABLE Parcelas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT,
    total INT,
    valor DECIMAL(10,2),
    data VARCHAR(15)
);

CREATE TABLE Transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(15),
    parcelaId INT,
    FOREIGN KEY (parcelaId) REFERENCES Parcelas(id)
);

CREATE TABLE Cartoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    finalCartao INT,
    transacaoId INT,
    FOREIGN KEY (transacaoId) REFERENCES Transacoes(id)
);

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    cartaoId INT,
    FOREIGN KEY (cartaoId) REFERENCES Cartoes(id)
);

CREATE TABLE Categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(30),
    transacaoId INT,
    FOREIGN KEY (transacaoId) REFERENCES Transacoes(id)
);

```

#

### Instalar Dependências

- pip install -r requirements.txt

### Run

- python main.py

