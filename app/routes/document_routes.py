from flask import Blueprint, request, jsonify
from app.schemas.document_schema import DocumentSchema
from app.services.document_service import create_document, search_documents
from datetime import datetime


bp = Blueprint('documents', __name__, url_prefix="/documentos")
schema = DocumentSchema()
schema_many = DocumentSchema(many=True)

@bp.route("", methods=["POST"])
def create_doc():
    payload = request.get_json()
    errors = schema.validate(payload)
    if errors:
        return jsonify({'erros':errors}), 400
    payload['data'] = datetime.strptime(payload['data'], "%Y-%m-%d").date()
    doc = create_document(payload)
    return schema.dump(doc),201