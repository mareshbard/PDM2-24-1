from pydantic import BaseModel

class AlunoBase(BaseModel):
    aluno_nome: str
    endereco: str

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class Config:
        orm_mode = True
