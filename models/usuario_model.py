from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: Optional[str] = None
    nome: Optional[str] = None
    cpf: Optional[int] = None
    cnpj: Optional[int] = None
    data_nascimento: Optional[str] = None
    email: Optional[str] = None
    telefone:Optional[int] = None
    cep: Optional[int] = None
    senha: Optional[str] = None
    perfil: Optional[int] = None
    token: Optional[str] = None
    credito: Optional[int] = None
