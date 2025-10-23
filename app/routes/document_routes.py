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











