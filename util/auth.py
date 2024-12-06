import os
from typing import Optional
import bcrypt
from fastapi.responses import RedirectResponse
import jwt
from datetime import datetime
from datetime import timedelta
from fastapi import HTTPException, Request, status

from dtos.usuario_autenticado import UsuarioAutenticado

NOME_COOKIE_AUTH = "jwt-token"

# async def obter_usuario_logado(request: Request) -> dict:
#     try:
#         token = request.cookies[NOME_COOKIE_AUTH]
#         if token.strip() == "":
#             return None
#         dados = validar_token_jwt(token)
#         usuario = UsuarioAutenticado(
#             nome = dados["nome"], 
#             email = dados["email"], 
#             perfil= dados["perfil"])
#         if "mensagem" in dados.keys():
#             usuario.mensagem = dados["mensagem"]
#         return usuario
#     except KeyError:
#         return None
    

async def checar_autenticacao(request: Request, call_next):
    token = request.cookies.get("jwt_token", None)
    if token:
        usuario_autenticado_dto = decodificar_token_jwt(token)
        request.state.usuario = usuario_autenticado_dto
    response = await call_next(request)
    return response

async def checar_autorizacao(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    area_da_empresa = request.url.path.startswith("/empresa")
    area_do_admin = request.url.path.startswith("/admin")
    area_do_centro_de_coleta = request.url.path.startswith("/centro")
    area_do_consumidor = request.url.path.startswith("/consumidor")
    if (area_da_empresa or area_do_admin or area_do_centro_de_coleta or area_do_consumidor) and (not usuario or not usuario.perfil):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if area_da_empresa and usuario.perfil != 2:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_admin and usuario.perfil != 3:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_centro_de_coleta and usuario.perfil != 4:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_consumidor and usuario.perfil != 5:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

def criar_token_jwt(usuarioAutenticado: UsuarioAutenticado) -> str:
    dados_token = {
        "id": usuarioAutenticado.id,
        "nome": usuarioAutenticado.nome,
        "email": usuarioAutenticado.email,
        "perfil": usuarioAutenticado.perfil,
        "credito": usuarioAutenticado.credito,
        "exp": datetime.now() + timedelta(days=1),
    }
    secret_key = os.getenv("JWT_TOKEN_SECRET")
    return jwt.encode(dados_token, secret_key, "HS256")


def decodificar_token_jwt(token: str) -> Optional[UsuarioAutenticado]:
    secret_key = os.getenv("JWT_TOKEN_SECRET")
    try:
        dados_token = jwt.decode(token, secret_key, "HS256")
        return UsuarioAutenticado(
            id=int(dados_token["id"]),
            nome=dados_token["nome"],
            email=dados_token["email"],
            perfil=int(dados_token["perfil"]),
        )
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def adicionar_token_jwt(response: RedirectResponse, token: str):
    response.set_cookie(
        key="jwt_token",
        value=token,
        max_age=3600 * 24,
        httponly=True,
        samesite="strict",
    )


def remover_token_jwt(response: RedirectResponse):
    response.set_cookie(
        key="jwt_token",
        value="",
        max_age=0,
        httponly=True,
        samesite="strict",
    )


async def checar_autenticacao(request: Request, call_next):
    token = request.cookies.get("jwt_token", None)
    if token:
        usuario_autenticado_dto = decodificar_token_jwt(token)
        request.state.usuario = usuario_autenticado_dto
    response = await call_next(request)
    return response
