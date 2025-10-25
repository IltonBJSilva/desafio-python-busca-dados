from marshmallow import Schema, fields, validate


class DocumentSchema(Schema):
    """
    Schema para validação e serialização de documentos.

    Campos:
        - id (int, dump_only): ID do documento, gerado automaticamente pelo banco.
        - titulo (str, obrigatório): Título do documento, mínimo de 1 caractere.
        - autor (str, opcional): Autor do documento, pode ser None.
        - conteudo (str, obrigatório): Conteúdo textual do documento.
        - data (date, obrigatório): Data do documento, no formato YYYY-MM-DD.
        - latitude (float, opcional): Latitude do local associado ao documento.
        - longitude (float, opcional): Longitude do local associado ao documento.
    """
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(min=1))
    autor = fields.Str(required=False, allow_none=True)
    conteudo = fields.Str(required=True)
    data = fields.Date(required=True, format="%Y-%m-%d")
    latitude = fields.Float(required=False, allow_none=True)
    longitude = fields.Float(required=False, allow_none=True)