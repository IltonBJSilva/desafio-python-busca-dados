# app/database/connection.py
"""
Módulo de configuração do banco de dados usando SQLAlchemy.

Fornece:
- engine: Conexão com o banco.
- SessionLocal: Factory de sessões para interagir com o banco.
- Base: Classe base para os modelos ORM.
- init_db(): Função helper para criar todas as tabelas definidas.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Pega a URL do banco do .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./desafio.db")

# Cria engine SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Cria sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Função helper pra criar todas as tabelas
def init_db():
    """
    Inicializa o banco de dados criando todas as tabelas definidas nos modelos ORM.

    Deve ser chamada no início da aplicação para garantir que as tabelas existam.
    """
    Base.metadata.create_all(bind=engine)
