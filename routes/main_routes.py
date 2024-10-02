from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha

router = APIRouter()
templates = Jinja2Templates("templates")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/index.html", view_model)

@router.get("/login")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/login.html", view_model)

@router.post("/post_entrar_consumidor")
async def post_entrar_consumidor(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/loginconsumidor", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2])
    nome_perfil = None
    match (usuario[2]):
        case 1: nome_perfil = "usuario"
        case 2: nome_perfil = "empresa"
        case 3: nome_perfil = "admin"
        case 4: nome_perfil = "centrodecoleta"
        case 5: nome_perfil = "consumidor"
        case _: nome_perfil = ""
    response = RedirectResponse(f"/{nome_perfil}/perfil", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.post("/post_entrar_empresa")
async def post_entrar_empresa(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse(f"/{nome_perfil}", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2])
    nome_perfil = None
    match (usuario[2]):
        case 1: nome_perfil = "consumidor"
        case 2: nome_perfil = "empresa"
        case 3: nome_perfil = "admin"
        case 4: nome_perfil = "centrodecoleta"
        case _: nome_perfil = ""
        
    response = RedirectResponse("/empresa/perfilempresa", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.post("/post_entrar_admin")
async def post_entrar_admin(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/loginadmin", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2])
    nome_perfil = None
    match (usuario[2]):
        case 1: nome_perfil = "consumidor"
        case 2: nome_perfil = "empresa"
        case 3: nome_perfil = "admin"
        case 4: nome_perfil = "centrodecoleta"
        case _: nome_perfil = ""
        
    response = RedirectResponse(f"/{nome_perfil}", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.post("/post_entrar_centrodecoleta")
async def post_entrar_centrodecoleta(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/logincentrodecoleta", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2])
    nome_perfil = None
    match (usuario[2]):
        case 1: nome_perfil = "consumidor"
        case 2: nome_perfil = "empresa"
        case 3: nome_perfil = "admin"
        case 4: nome_perfil = "centrodecoleta"
        case _: nome_perfil = ""
        
    response = RedirectResponse(f"/{nome_perfil}/addcreditos", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.get("/loginempresa")
async def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/loginempresa.html", view_model)

@router.get("/loginadmin")
async def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/loginadmin.html", view_model)

@router.get("/loginconsumidor")
async def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/loginconsumidor.html", view_model)

@router.get("/logincentrodecoleta")
async def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/logincentrodecoleta.html", view_model)

@router.get("/criarconta1")
async def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/criarconta1.html", view_model)

@router.post("/post_cadastrar")
async def post_cadastrar(
    nome: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cep: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/criarconta1", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome, 
        cpf=cpf, 
        email=email, 
        telefone=telefone,
        cep=cep, 
        senha=senha_hash,
        perfil=5)
    UsuarioRepo.inserir(usuario)
    return RedirectResponse("/loginconsumidor", status_code=status.HTTP_303_SEE_OTHER)