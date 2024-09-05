from sqlalchemy.orm import Session
from models import Aluno
from schemas import AlunoCreate, AlunoUpdate

def create_aluno(db: Session, aluno: AlunoCreate):
    db_aluno = Aluno(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def get_alunos(db: Session):
    return db.query(Aluno).all()

def get_aluno(db: Session, aluno_id: int):
    return db.query(Aluno).filter(Aluno.id == aluno_id).first()

def update_aluno(db: Session, aluno_id: int, aluno: AlunoUpdate):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if db_aluno:
        for key, value in aluno.dict().items():
            setattr(db_aluno, key, value)
        db.commit()
        db.refresh(db_aluno)
    return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if db_aluno:
        db.delete(db_aluno)
        db.commit()
    return db_aluno
