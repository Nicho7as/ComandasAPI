from pydantic import BaseModel
#Nicholas

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str = None
    valor_unitario: float
    foto: str = None