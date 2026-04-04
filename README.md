# System Bank API

API bancária em Python com arquitetura MVC, suporte a Pessoa Física e Pessoa Jurídica, persistência em SQLite e testes unitários.

## Objetivo

Este projeto implementa uma API para operações bancárias básicas com:

- cadastro de clientes Pessoa Física
- cadastro de clientes Pessoa Jurídica
- listagem de clientes
- consulta por identificador
- atualização de saldo
- saque
- extrato

O projeto foi estruturado seguindo o padrão MVC trabalhado no curso, com separação entre `main`, `views`, `controllers`, `models`, `validators` e `errors`.

## Tecnologias

- Python 3.14
- Flask
- Flask-CORS
- SQLAlchemy
- SQLite
- Pytest
- mock-alchemy

## Arquitetura

### Camadas

- `src/main`
  Inicialização da aplicação, composição das dependências e registro das rotas.
- `src/views`
  Recebe `HttpRequest`, valida entrada e devolve `HttpResponse`.
- `src/controllers`
  Orquestra o fluxo da aplicação e formata as respostas.
- `src/models`
  Entidades, interfaces de repositório e persistência SQLite.
- `src/validators`
  Validação dos dados de entrada por caso de uso.
- `src/errors`
  Exceções específicas da aplicação.

### Fluxo

1. A rota Flask recebe a requisição.
2. A rota cria um `HttpRequest`.
3. A view valida a entrada e chama o controller.
4. O controller aciona o repositório.
5. O repositório acessa o banco SQLite.
6. A resposta volta em formato `HttpResponse`.

## Estrutura de pastas

```text
.
├── run.py
├── requirements.txt
├── storage.db
├── README.md
└── src
    ├── main
    │   ├── composer
    │   ├── routes
    │   └── server
    ├── views
    │   ├── http_types
    │   └── interface
    ├── controllers
    ├── models
    │   └── sqlite
    ├── validators
    └── errors
```

## Requisitos para executar

- Python 3.14 instalado
- `pip` disponível no ambiente

## Instalação

Clone o projeto e, na raiz, execute:

```bash
python -m pip install -r requirements.txt
```

## Execução do projeto

Inicie a aplicação com:

```bash
python run.py
```

Por padrão, a API sobe em:

```text
http://127.0.0.1:3000
```

O banco SQLite é criado automaticamente no arquivo:

```text
storage.db
```

## Execução dos testes

Para rodar a suíte:

```bash
pytest -q
```

## Rotas disponíveis

### Pessoa Física

Base:

```text
/pessoa_fisica
```

Rotas:

- `GET /pessoa_fisica/`
- `POST /pessoa_fisica/`
- `GET /pessoa_fisica/<id>`
- `PATCH /pessoa_fisica/<id>/saldo`
- `POST /pessoa_fisica/<id>/sacar`
- `GET /pessoa_fisica/<id>/extrato`

Exemplo de criação:

```json
{
  "renda_mensal": 5000.0,
  "idade": 30,
  "nome_completo": "Joao Silva",
  "celular": "11999999999",
  "categoria": "A",
  "saldo": 1000.0
}
```

Exemplo de saque:

```json
{
  "valor": 100.0
}
```

Exemplo de ajuste de saldo:

```json
{
  "saldo": 1500.0
}
```

### Pessoa Jurídica

Base:

```text
/pessoa_juridica
```

Rotas:

- `GET /pessoa_juridica/`
- `POST /pessoa_juridica/`
- `GET /pessoa_juridica/<id>`
- `PATCH /pessoa_juridica/<id>/saldo`
- `POST /pessoa_juridica/<id>/sacar`
- `GET /pessoa_juridica/<id>/extrato`

Exemplo de criação:

```json
{
  "razao_social": "Empresa XPTO LTDA",
  "nome_fantasia": "XPTO",
  "cnpj": "12.345.678/0001-99",
  "email": "contato@xpto.com",
  "limit_saque": 5000.0
}
```

Exemplo de saque:

```json
{
  "valor": 300.0
}
```

Exemplo de ajuste de saldo:

```json
{
  "saldo": 2000.0
}
```

## Regras de negócio implementadas

- conexão com banco SQLite
- interface `Cliente` com `sacar` e `extrato`
- testes unitários para controllers
- criação e listagem de usuários
- limite de saque diferente entre PF e PJ
  - Pessoa Física: `1000.00`
  - Pessoa Jurídica: `5000.00`

## Formato de resposta

As respostas da aplicação seguem este padrão:

```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {}
  }
}
```

## Observações

- O arquivo `storage.db` pode ser recriado automaticamente pela aplicação.
- O projeto possui testes unitários cobrindo controllers, repositories e conexão.
- Há um arquivo `src/main/routes/routes.py` mantido como apoio estrutural, mas o registro principal de blueprints está centralizado em `src/main/server/server.py`.

## Comandos úteis

Instalar dependências:

```bash
python -m pip install -r requirements.txt
```

Executar API:

```bash
python run.py
```

Executar testes:

```bash
pytest -q
```
