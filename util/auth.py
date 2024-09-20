import os
import bcrypt
import jwt
from datetime import datetime
from datetime import timedelta
from fastapi import HTTPException, Request, status

from dtos.usuario_autenticado import UsuarioAutenticado

NOME_COOKIE_AUTH = "jwt-token"

async def obter_usuario_logado(request: Request) -> dict:
    try:
        token = request.cookies[NOME_COOKIE_AUTH]
        if token.strip() == "":
            return None
        dados = validar_token(token)
        usuario = UsuarioAutenticado(
            nome = dados["nome"], 
            email = dados["email"], 
            perfil= dados["perfil"])
        if "mensagem" in dados.keys():
            usuario.mensagem = dados["mensagem"]
        return usuario
    except KeyError:
        return None
    

async def checar_autenticacao(request: Request, call_next):
    usuario = await obter_usuario_logado(request)
    request.state.usuario = usuario
    response = await call_next(request)
    if response.status_code == status.HTTP_307_TEMPORARY_REDIRECT:
        return response
    return response


async def checar_autorizacao(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    area_do_usuario = request.url.path.startswith("/usuario")
    area_da_empresa = request.url.path.startswith("/empresa")
    area_do_admin = request.url.path.startswith("/admin")
    area_do_centro = request.url.path.startswith("/centro")
    area_do_consumidor = request.url.path.startswith("/usuario")
    if (area_do_usuario or area_da_empresa or area_do_admin or area_do_centro or area_do_consumidor) and not usuario.perfil:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if area_do_usuario and usuario.perfil != 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_da_empresa and usuario.perfil != 2:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_admin and usuario.perfil != 3:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_centro and usuario.perfil != 4:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_consumidor and usuario.perfil != 5:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

def obter_hash_senha(senha: str) -> str:
    try:
        hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return hashed.decode()
    except ValueError:
        return ""


def conferir_senha(senha: str, hash_senha: str) -> bool:
    try:
        return bcrypt.checkpw(senha.encode(), hash_senha.encode())
    except ValueError:
        return False
    

def criar_token(nome: str, email: str, perfil: int) -> str:
    payload = {
        "nome": nome,
        "email": email,
        "perfil": perfil,
        "exp": datetime.now() + timedelta(days=1)
    }
    return jwt.encode(payload, 
        os.getenv("JWT_SECRET"),
        os.getenv("JWT_ALGORITHM"))


def validar_token(token: str) -> dict:
    try:
        return jwt.decode(token, 
            os.getenv("JWT_SECRET"),
            os.getenv("JWT_ALGORITHM"))
    except jwt.ExpiredSignatureError:
        return { "nome": None, "email": None, "perfil": 0, "mensagem": "Token expirado" }
    except jwt.InvalidTokenError:
        return { "nome": None, "email": None, "perfil": 0, "mensagem": "Token inválido" }        
    except Exception as e:
        return { "nome": None, "email": None, "perfil": 0, "mensagem": f"Erro: {e}" }
    

def criar_cookie_auth(response, token):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=1800,
        httponly=True,
        samesite="lax",
    )
    return response