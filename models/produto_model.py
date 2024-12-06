from dataclasses import dataclass
from typing import Optional


@dataclass
class Produto:
    id: Optional[str] = None
    nome: Optional[str] = None
    preco: Optional[int] = None
    descricao: Optional[int] = None
    id_empresa: Optional[str] = None
