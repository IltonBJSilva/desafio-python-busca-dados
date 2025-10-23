from app.database.connection import SessionLocal
from app.models.document import Document
from sqlalchemy import or_
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
        if busca:
            term = f"%{busca}"
            q = q.filter(
                or_(
                    Document.titulo.ilike(term),
                    Document.conteudo.ilike(term),
                    Document.autor.ilike(term)
                )
            )
        elif palavraChave:
            term = f"%{palavraChave}"
            q = q.filter(
                or_(
                    Document.titulo.ilike(term),
                    Document.conteudo.ilike(term),
                    Document.autor.ilike(term)
                )
            )
        results = q.all()
        if latitude is not None and longitude is not None:
            results.sort(key=lambda d: distance_km(latitude, longitude, d.latitude, d.longitude))
        return results
    finally:
        db.close()
