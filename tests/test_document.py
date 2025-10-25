from datetime import date
import pytest
from app.database.connection import SessionLocal
from app.models.document import Document
from app.services.document_service import create_document, search_documents

# ------------------------
# Fixtures para teste
# ------------------------

@pytest.fixture
def db():
    #Usa sessão temporária
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
    


@pytest.fixture   
def sample_document():
    return{
        "titulo": "Carros antigos em Porto Alegre",
        "autor": "João Mecânico",
        "conteudo": "Um encontro será realizado com carros antigos na cidade.",
        "latitude": -30.0346,
        "longitude": -51.2177,
        "data": date(2025, 10, 24)  # <--- aqui é um datetime.date
    }   

# ------------------------
# Testes de criação
# ------------------------ 
def test_create_document(db, sample_document):
    doc = create_document(sample_document)
    assert doc.id is not None
    assert doc.titulo == sample_document["titulo"]
    assert doc.autor == sample_document["autor"]




















