"""
Módulo de rotas para documentos.

Fornece endpoints para:
- Criar documentos (POST)
- Buscar documentos (GET)
"""
from flask import Blueprint, request, jsonify
from app.schemas.document_schema import DocumentSchema
from app.services.document_service import create_document, search_documents
from datetime import datetime
import math


bp = Blueprint('documents', __name__, url_prefix="/documentos")
schema = DocumentSchema()
schema_many = DocumentSchema(many=True)


# ========================
# POST - Criar Documento
# ========================
@bp.route("", methods=["POST"])
def create_doc():
    """
    Cria um novo documento no banco de dados.

    Espera um JSON com:
    - titulo (str, obrigatório)
    - autor (str, opcional)
    - conteudo (str, obrigatório)
    - data (str, obrigatório, formato YYYY-MM-DD)
    - latitude (float, opcional)
    - longitude (float, opcional)

    Valida o payload, converte a data e cria o documento usando o service.

    Retorna:
        JSON do documento criado e status 201
        ou JSON com erros e status 400 se houver validação
    """
    payload = request.get_json()
    errors = schema.validate(payload)
    if errors:
        return jsonify({'erros':errors}), 400
    payload['data'] = datetime.strptime(payload['data'], "%Y-%m-%d").date()
    doc = create_document(payload)
    return schema.dump(doc),201


# ========================
# GET - Buscar Documentos
# ========================
@bp.route("", methods=["GET"])
def search_doc():
    """
    Busca documentos no banco de dados.

    Parâmetros de query:
    - palavraChave (str, opcional)
    - busca (str, opcional)
    - latitude (float, opcional)
    - longitude (float, opcional)

    Regras:
    - Pelo menos 'palavraChave' ou 'busca' devem ser fornecidos
    - Se latitude e longitude forem fornecidas, os resultados são ordenados por proximidade

    Retorna:
        JSON com a lista de documentos encontrados e status 200
        ou JSON com erro e status 400 se os parâmetros obrigatórios não forem fornecidos
    """
    palavra_chave = request.args.get("palavraChave")
    busca = request.args.get("busca")
    lat_user = request.args.get("latitude", type=float)
    lon_user = request.args.get("longitude", type=float)

    if not palavra_chave and not busca:
        return jsonify({"erros": "O parâmetro 'palavraChave' ou 'busca' é obrigatório."}), 400

    # Passa pro service com nomes corretos
    resultados = search_documents(
        palavraChave=palavra_chave,
        busca=busca,
        latitude=lat_user,
        longitude=lon_user
    )

    # Ordena por proximidade se latitude/longitude forem fornecidas
    if lat_user is not None and lon_user is not None:
        resultados.sort(
            key=lambda doc: math.sqrt(
                (doc.latitude - lat_user)**2 + (doc.longitude - lon_user)**2
            ) if doc.latitude is not None and doc.longitude is not None else float('inf')
        )

    # Sempre retorna resultados
    return jsonify(schema_many.dump(resultados)), 200











