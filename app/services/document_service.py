from app.database.connection import SessionLocal
from app.models.document import Document
from sqlalchemy import or_, func
from app.utils.geo_utils import distance_km


def create_document(data_dict):
    db = SessionLocal()
    try:
        doc = Document(**data_dict)
        db.add(doc)
        db.commit()
        db.refresh(doc)
        return doc
    finally:
        db.close()


def search_documents(palavraChave=None, busca=None, latitude=None, longitude=None):
    db = SessionLocal()
    try:
        q = db.query(Document)

        termos = []
        if busca:
            termos = busca.lower().split()
        elif palavraChave:
            termos = palavraChave.lower().split()

        print(f"\n🔍 Termos de busca usados: {termos}\n")  # <-- debug

        # Para cada palavra, adiciona filtro OR em título, conteúdo ou autor
        for palavra in termos:
            q = q.filter(
                or_(
                    func.lower(Document.titulo).like(f"%{palavra}%"),
                    func.lower(Document.conteudo).like(f"%{palavra}%"),
                    func.lower(Document.autor).like(f"%{palavra}%")
                )
            )

        # Mostra o SQL que o SQLAlchemy vai rodar
        print(f"📜 SQL gerado: {str(q)}\n")

        results = q.all()
        print(f"📦 Resultados encontrados: {len(results)}\n")

        if latitude is not None and longitude is not None:
            results.sort(
                key=lambda d: distance_km(latitude, longitude, d.latitude, d.longitude)
            )

        return results
    finally:
        db.close()
