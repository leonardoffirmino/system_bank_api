CREATE TABLE IF NOT EXISTS pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    renda_mensal REAL,
    idade INTEGER,
    nome_completo TEXT,
    celular TEXT,
    email TEXT,
    categoria TEXT,
    saldo REAL
);

CREATE TABLE IF NOT EXISTS pessoas_juridicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    razao_social TEXT NOT NULL,
    nome_fantasia TEXT,
    cnpj TEXT NOT NULL UNIQUE,
    email TEXT,
    limite_saque REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    tipo_cliente TEXT NOT NULL,
    tipo_transacao TEXT NOT NULL,
    valor REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);