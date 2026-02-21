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

CREATE TABLE IF NOT EXISTS pessoas_juridica (
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

INSERT INTO
    pessoa_fisica (
        renda_mensal,
        idade,
        nome_completo,
        celular,
        email,
        categoria,
        saldo
    )
VALUES (
        4500.00,
        28,
        'Carlos Eduardo Lima',
        '(11) 98765-4321',
        'carlos.lima@email.com',
        'Gold',
        3200.00
    ),
    (
        3200.00,
        35,
        'Amanda Ferreira Souza',
        '(21) 99876-1234',
        'amanda.souza@email.com',
        'Silver',
        1500.00
    ),
    (
        7800.00,
        42,
        'Ricardo Alves Martins',
        '(31) 97654-8899',
        'ricardo.martins@email.com',
        'Platinum',
        12000.00
    ),
    (
        2500.00,
        23,
        'Juliana Rocha Santos',
        '(41) 98888-7766',
        'juliana.santos@email.com',
        'Basic',
        800.00
    ),
    (
        6200.00,
        30,
        'Felipe Henrique Costa',
        '(51) 97777-6655',
        'felipe.costa@email.com',
        'Gold',
        5400.00
    );

INSERT INTO
    pessoas_juridica (
        razao_social,
        nome_fantasia,
        cnpj,
        email,
        limite_saque
    )
VALUES (
        'Tech Solutions Brasil LTDA',
        'Tech Solutions',
        '11222333000101',
        'contato@techsolutions.com',
        15000.00
    ),
    (
        'Alimentos Prime Distribuidora LTDA',
        'Prime Distribuidora',
        '22333444000102',
        'financeiro@primealimentos.com',
        25000.00
    ),
    (
        'Construtora Horizonte S.A.',
        'Horizonte Engenharia',
        '33444555000103',
        'contato@horizonteengenharia.com',
        50000.00
    ),
    (
        'Marketing Digital Impacto LTDA',
        'Impacto MKT',
        '44555666000104',
        'atendimento@impactomkt.com',
        12000.00
    ),
    (
        'Transportes Rápido Sul LTDA',
        'Rápido Sul Logística',
        '55666777000105',
        'financeiro@rapidosul.com',
        30000.00
    );

INSERT INTO
    transacoes (
        cliente_id,
        tipo_cliente,
        tipo_transacao,
        valor
    )
VALUES (1, 'PF', 'SAQUE', 500.00),
    (2, 'PF', 'SAQUE', 200.00),
    (3, 'PF', 'SAQUE', 1000.00),
    (1, 'PJ', 'SAQUE', 5000.00),
    (4, 'PJ', 'SAQUE', 8000.00);