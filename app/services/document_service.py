from app.database.connection import SessionLocal
from app.models.document import Document
from sqlalchemy import or_, func
from app.utils.geo_utils import distance_km


def create_document(data_dict):
    """
    Cria e persiste um novo documento no banco de dados.

    Args:
        data_dict (dict): Dicionário contendo os campos do documento
                          Ex.: {"titulo": "...", "autor": "...", "conteudo": "...", "latitude": ..., "longitude": ...}

    Returns:
        Document: Objeto Document recém-criado e persistido no banco.

    Raises:
        sqlalchemy.exc.SQLAlchemyError: Se houver erro na operação de banco de dados.
    """
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
    """
    Realiza busca de documentos por palavra-chave ou texto, com opção de ordenação
    por proximidade geográfica caso latitude e longitude sejam fornecidas.

    Args:
        palavraChave (str, opcional): Palavra-chave para buscar no título, conteúdo ou autor.
        busca (str, opcional): Texto completo para busca.
        latitude (float, opcional): Latitude para cálculo de proximidade.
        longitude (float, opcional): Longitude para cálculo de proximidade.

    Returns:
        list[Document]: Lista de objetos Document que correspondem à busca,
                        ordenados pela proximidade geográfica se latitude e longitude forem fornecidas.

    Exemplo:
        search_documents(busca="carros antigos", latitude=-30.03, longitude=-51.23)
    """
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
