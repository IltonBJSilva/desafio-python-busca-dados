from flask import Flask
from app.routes.document_routes import bp as document_bp
from app.database.connection import engine, Base


def create_app():
    app = Flask(__name__)
    app.register_blueprint(document_bp)
    Base.metadata.create_all(bind=engine)
    return app
app = create_app()


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)