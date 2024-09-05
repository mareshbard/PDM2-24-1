from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./dbalunos.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição do modelo Aluno
class Aluno(Base):
    __tablename__ = "TB_ALUNO"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    aluno_nome = Column(String(50), index=True)
    endereco = Column(String(100))

# Criação das tabelas no banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)
