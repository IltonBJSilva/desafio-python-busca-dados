# app/database/connection.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
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
    Base.metadata.create_all(bind=engine)
