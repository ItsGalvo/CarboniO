from dataclasses import dataclass
from typing import Optional


@dataclass
class Cupom:
    id: Optional[str] = None
    nome: Optional[str] = None
    valor: Optional[int] = None
    descricao: Optional[int] = None
    id_empresa: Optional[str] = None
    imagem: Optional[str] = None
