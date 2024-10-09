from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import obter_hash_senha

router = APIRouter(prefix="/admin")
templates = Jinja2Templates("templates")

@router.get("/index_adm")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/index_adm.html", view_model)

@router.get("/addempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/addempresa.html", view_model)

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
        return RedirectResponse("/addempresa", status_code=status.HTTP_303_SEE_OTHER)
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
    return RedirectResponse("/index_adm", status_code=status.HTTP_303_SEE_OTHER)