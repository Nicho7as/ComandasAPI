from pydantic import BaseModel
#Nicholas

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str