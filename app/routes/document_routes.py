from flask import Blueprint, request, jsonify
from app.schemas.document_schema import DocumentSchema
from app.services.document_service import create_document, search_documents


bp = Blueprint('documents', __name__, url_prefix="/documentos")
schema = DocumentSchema()
schema_many = DocumentSchema(Many=True)

@bp.route("", methods=["POST"])
def create_doc():
    payload = request.get_json()
    errors = schema.validate(payload)
    if errors:
        return jsonify({'erros':errors}), 400
    doc = create_document(payload)
    return schema.dump(doc),201