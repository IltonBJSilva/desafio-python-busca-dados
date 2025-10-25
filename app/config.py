import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define a URL de conexão com o banco de dados.
# Caso não haja variável DATABASE_URL no .env, usa um PostgreSQL local como padrão.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/desafio_db"
)
