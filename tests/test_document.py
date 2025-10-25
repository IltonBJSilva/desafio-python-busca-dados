from datetime import date
import pytest
from app.database.connection import SessionLocal
from app.models.document import Document
from app.services.document_service import create_document, search_documents
import time

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
    
"""

@pytest.fixture   
def sample_document():
    return{
        "titulo": "Carros antigos em Porto Alegre",
        "autor": "João Mecânico",
        "conteudo": "Um encontro será realizado com carros antigos na cidade.",
        "latitude": -30.0346,
        "longitude": -51.2177,
        "data": date(2025, 10, 24) 
    }   

# ------------------------
# Testes de criação
# ------------------------ 

#Funcinou 100%
def test_create_document(db, sample_document):
    doc = create_document(sample_document)
    assert doc.id is not None
    assert doc.titulo == sample_document["titulo"]
    assert doc.autor == sample_document["autor"]


# ------------------------
# Testes de busca
# ------------------------
def test_search_by_titulo(db, sample_document):
    results = search_documents(busca="carros antigos")
    assert len(results) > 0
    assert any("Carros antigos" in d.titulo for d in results)


def test_search_by_conteudo(db, sample_document):
    results = search_documents(busca="encontro será realizado")
    assert len(results) > 0
    assert any("encontro será realizado" in d.conteudo for d in results)

def test_search_by_autor(db, sample_document):
    results = search_documents(busca="João Mecânico")
    assert len(results) > 0
    assert any("João Mecânico" in d.autor for d in results)

# ------------------------
# Teste busca sem resultados
# ------------------------

def test_search_no_results(db):
    results = search_documents(busca="não existente")
    assert len(results) == 0


# ------------------------
# Teste busca com coordenadas
# ------------------------
def test_search_with_coordinates(db, sample_document):
    results = search_documents(busca="carros", latitude=-30.0346, longitude=-51.2177)
    assert len(results) > 0
    #Verificar se a primeira posição é o documento mais proximo
    assert results[0].titulo == sample_document["titulo"]
"""

# ------------------------
# Teste performance
# ------------------------
def test_performance_bulk_inserts(db):
    start = time.time()
    # Insere 1000 documentos
    for i in range(1000):
        create_document({
            "titulo": f"Doc {i}",
            "autor": "Tester",
            "conteudo": "Performance test",
            "data": date.today(),
        })
        print(f"✅ Criado Doc {i}")

    # Agora busca tudo de uma vez
    results = search_documents(busca="Doc")
    duration = time.time() - start

    print(f"📦 Documentos encontrados: {len(results)}")
    # Testa se inseriu tudo
    assert len(results) == 1000, f"Foram encontrados {len(results)} documentos, esperava 1000."
    # Testa performance
    assert duration < 6, f"A inserção demorou {duration:.2f}s, muito lenta!"



