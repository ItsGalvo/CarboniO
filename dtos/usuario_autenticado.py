from dataclasses import dataclass
from typing import Optional


@dataclass
class UsuarioAutenticado:
    id: Optional[int] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    perfil: Optional[int] = None
    credito: Optional[int] = None
