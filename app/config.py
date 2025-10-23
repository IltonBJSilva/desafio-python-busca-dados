import os
from dotenv import load_dotenv

load_dotenv #Carrega a .env

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/desafio_db")