from marshmallow import Schema, fields, validate


class DocumentSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(min=1))
    autor = fields.Str(required=False, allow_none=True)
    conteudo = fields.Str(required=True)
    data = fields.Date(required=True, format="%Y-%m-%d")
    latitude = fields.Float(required=False, allow_none=True)
    longitude = fields.Float(required=False, allow_none=True)