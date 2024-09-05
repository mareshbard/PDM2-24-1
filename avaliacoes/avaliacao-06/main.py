from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import init_db, SessionLocal
from crud import create_aluno, get_alunos, get_aluno, update_aluno, delete_aluno
from schemas import AlunoCreate, AlunoUpdate

app = FastAPI()

# Inicializa o banco de dados
init_db()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para criar um novo aluno
@app.post("/alunos/", response_model=AlunoCreate)
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    return create_aluno(db=db, aluno=aluno)

# Endpoint para listar todos os alunos
@app.get("/alunos/")
def listar_alunos(db: Session = Depends(get_db)):
    return get_alunos(db=db)

# Endpoint para listar um aluno por id
@app.get("/alunos/{aluno_id}")
def listar_um_aluno(aluno_id: int, db: Session = Depends(get_db)):
    return get_aluno(db=db, aluno_id=aluno_id)

# Endpoint para atualizar um aluno por id
@app.put("/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: int, aluno: AlunoUpdate, db: Session = Depends(get_db)):
    return update_aluno(db=db, aluno_id=aluno_id, aluno=aluno)

# Endpoint para excluir um aluno por id
@app.delete("/alunos/{aluno_id}")
def excluir_aluno(aluno_id: int, db: Session = Depends(get_db)):
    return delete_aluno(db=db, aluno_id=aluno_id)
