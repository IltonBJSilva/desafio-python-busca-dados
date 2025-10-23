## 🗂️ Estrutura do Projeto

```bash
desafio-python-busca-dados/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # ponto de entrada da aplicação (FastAPI, Flask, etc)
│   ├── config.py            # configs de ambiente (DB, etc)
│   │
│   ├── models/              # modelos do banco de dados
│   │   ├── __init__.py
│   │   └── document.py
│   │
│   ├── schemas/             # validação (Pydantic ou Marshmallow)
│   │   ├── __init__.py
│   │   └── document_schema.py
│   │
│   ├── routes/              # endpoints da API
│   │   ├── __init__.py
│   │   └── document_routes.py
│   │
│   ├── services/            # lógica de negócio (busca, ordenação, etc)
│   │   ├── __init__.py
│   │   └── document_service.py
│   │
│   ├── utils/               # funções auxiliares (ex: cálculo de distância)
│   │   ├── __init__.py
│   │   └── geo_utils.py
│   │
│   └── database/
│       ├── __init__.py
│       └── connection.py    # conexão com o banco (SQLAlchemy, psycopg, etc)
│
├── tests/                   # testes unitários e de integração
│   ├── __init__.py
│   └── test_document.py
│
├── requirements.txt          # dependências do projeto
├── README.md                 # documentação
└── .env.example              # exemplo de variáveis de ambiente (DB_URL, etc)
```
