from sqlalchemy import Column, Integer, String, Text, Date, Float
from app.database.connection import Base



#Criar uma classe para definir os dados dentro de uma tabela do banco
class Document(Base):
    __tablename__ = "documents"
    #define estrutura da tabela, tipos de dados e constraints.
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=True)
    conteudo = Column(Text, nullable=False)
    data = Column(Date, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    