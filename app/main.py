# app/main.py

from flask import Flask
from app.routes.document_routes import bp as document_bp
from app.database.connection import init_db

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    # Registrar blueprint de documentos
    app.register_blueprint(document_bp)

    # Inicializa o banco (cria tabelas se não existirem)
    init_db()

    return app

# Cria a app
app = create_app()

if __name__ == "__main__":
    # Roda o servidor Flask
    app.run(debug=True, host="0.0.0.0", port=5000)
