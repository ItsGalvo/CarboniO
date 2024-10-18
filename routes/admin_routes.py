from urllib import response
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import obter_hash_senha
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso

router = APIRouter(prefix="/admin")
templates = Jinja2Templates("templates")

@router.get("/index")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/index.html", view_model)

@router.get("/addempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/addempresa.html", view_model)

@router.get("/addcentrocoleta")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/addcentrocoleta.html", view_model)

@router.post("/post_cadastrar_empresa")
async def post_cadastrar_empresa(
    nome: str = Form(...),
    cnpj: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cep: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        response = RedirectResponse("/admin/addempresa", status_code=status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Credenciais inválidas! Cheque os valores digitados e tente novamente.")
        return response
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome, 
        cnpj=cnpj, 
        email=email, 
        telefone=telefone,
        cep=cep, 
        senha=senha_hash,
        perfil=2)
    UsuarioRepo.inserir(usuario)
    response = RedirectResponse("/admin/index", status_code=status.HTTP_303_SEE_OTHER)
    adicionar_mensagem_sucesso(response, "Empresa cadastrada com sucesso!")
    return response

@router.post("/post_cadastrar_centrocoleta")
async def post_cadastrar_centrocoleta(
    nome: str = Form(...),
    cnpj: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cep: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        response = RedirectResponse("/admin/addcentrocoleta", status_code=status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Credenciais inválidas! Cheque os valores digitados e tente novamente.")
        return response
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome, 
        cnpj=cnpj, 
        email=email, 
        telefone=telefone,
        cep=cep, 
        senha=senha_hash,
        perfil=4)
    UsuarioRepo.inserir(usuario)
    response = RedirectResponse("/admin/index", status_code=status.HTTP_303_SEE_OTHER)
    adicionar_mensagem_sucesso(response, "Empresa cadastrada com sucesso!")
    return response