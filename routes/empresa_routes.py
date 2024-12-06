import bcrypt
from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.cupom_model import Cupom
from models.usuario_model import Usuario
from repositories.cupom_repo import CupomRepo
from repositories.usuario_repo import UsuarioRepo
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso

router = APIRouter(prefix="/empresa")
templates = Jinja2Templates("templates")

@router.get("/cuponsativos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/cuponsativos.html", view_model)

@router.get("/index")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/index.html", view_model)

@router.get("/editarperfilempresa")
def get_root(request: Request):
    usuario = request.state.usuario
    dados = UsuarioRepo.obter_dados_por_email(usuario.email)
    view_model = {"request": request, "dados": dados}
    return templates.TemplateResponse("main/pages/empresa/editarperfilempresa.html", view_model)

@router.post("/atualizar_dados")
async def post_dados(request: Request):
    dados = dict(await request.form())
    usuarioAutenticadoDto = (
        request.state.usuario if hasattr(request.state, "usuario") else None
    )
    dados["id"] = usuarioAutenticadoDto.id
    usuario = Usuario(**dados)
    if UsuarioRepo.atualizar_dados(usuario):
        response = RedirectResponse("/empresa/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro atualizado com sucesso!")
        return response
    else:
        response = RedirectResponse("/empresa/editarperfilempresa", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao atualizar seu cadastro. Tente novamente mais tarde.",
        )
        return response

@router.get("/adicionarcupom")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/adicionarcupom.html", view_model)

@router.get("/estatisticas")
def get_root(request: Request):
    options = [
        {"value": "2021", "label": "2021"},
        {"value": "2022", "label": "2022"},
        {"value": "2023", "label": "2023"},
        {"value": "2024", "label": "2024"},
    ]
    view_model = {"request": request, "options": options}
    return templates.TemplateResponse("main/pages/empresa/estatisticas.html", view_model)

@router.get("/mensagens")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/mensagens.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/politicaprivacidade.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/termosdeuso.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/contato.html", view_model)

@router.post("/alterar_senha")
async def post_alterarsenha(request: Request):
    dados = dict(await request.form())
    usuario = request.state.usuario
    id = usuario.id
    email = usuario.email
    senha = dados["senha"]
    novasenha = dados["novasenha"]
    confsenha = dados["confsenha"]
    senha_hash = UsuarioRepo.obter_senha_por_email(email)

    if not senha_hash:
        response = RedirectResponse("/empresa/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Usuário/senha não encontrado em nossa base de dados.")
        return response
    
    if not bcrypt.checkpw(senha.encode(), senha_hash.encode()):
        response = RedirectResponse("/empresa/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Senha atual não confere.")
        return response
    
    if novasenha != confsenha:
        response = RedirectResponse("/empresa/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Nova senha não foi confirmada com sucesso.")
        return response
    
    senha_hash = bcrypt.hashpw(novasenha.encode(), bcrypt.gensalt())
    UsuarioRepo.atualizar_senha(id, senha_hash.decode())
    response = RedirectResponse("/empresa/index", status.HTTP_303_SEE_OTHER)
    adicionar_mensagem_sucesso(response, "Senha alterada com sucesso!")
    return response

@router.post("/cadastrar_cupom")
async def post_cadastrar_cupom(request: Request):
    dados = dict(await request.form())
    empresa = request.state.usuario
    id_empresa = empresa.id
    dados["id_empresa"] = id_empresa
    cupom = Cupom(**dados)
    cupom = CupomRepo.inserir(cupom)
    if cupom:
        response = RedirectResponse("/empresa/adicionarcupom", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "cupom cadastrado com sucesso!")
        return response
    else:
        response = RedirectResponse("/empresa/adicionarcupom", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao realizar o cadastro. Tente novamente.",
        )
        return response
